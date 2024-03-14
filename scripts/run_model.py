from transformers import AutoTokenizer, AutoModel
from IPython.display import display, Markdown, clear_output
import os
import torch
from transformers import AutoConfig


def display_answer(model, query, history=[]):
    for response, history in model.stream_chat(
            tokenizer, query, history=history):
        clear_output(wait=True)
        display(Markdown(response))
    return history


model_path = "/group/40034/palchenli/data/dcic/model/"
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

config = AutoConfig.from_pretrained(model_path, trust_remote_code=True, pre_seq_len=128)
model = AutoModel.from_pretrained(model_path, config=config, trust_remote_code=True)
prefix_state_dict = torch.load("/group/40034/palchenli/data/dcic/chatglm2/ChatGLM2-6B/ptuning/output/adgen-chatglm2-6b-pt--/checkpoint-3000/pytorch_model.bin")
new_prefix_state_dict = {}
for k, v in prefix_state_dict.items():
    if k.startswith("transformer.prefix_encoder."):
        new_prefix_state_dict[k[len("transformer.prefix_encoder."):]] = v
model.transformer.prefix_encoder.load_state_dict(new_prefix_state_dict)

model = model.half().cuda()
model.transformer.prefix_encoder.float()
model = model.eval()

query = "你是一个医生，请根据患者的病例回答患者的问题。患者的病例为：男，63岁。;主诉：发现肝占位1天。;现病史：入院前1天因“消瘦”于当地医院检查彩超提示肝占位（未见报告单），无腹痛、腹胀、腹泻，无反酸、嗳气，无恶心、呕吐、呕血、黑便，无尿黄、眼黄、皮肤黄等不适，进一步我院查AFP 23.8ng/ml，异常凝血酶原 10161 mAU/ml；腹部彩超：肝内多发不均高回声团块或结节（考虑MT）；余肝内声像呈弥漫性病变；3、胆囊壁增厚毛糙；脾肿大。发病以来，精神、睡眠尚可，食欲、食量正常，大小便如常，近2个月体重减轻约6Kg。否认发病前有不洁饮食史，否认肝炎病人密切接触史。;既往史：10余年前“肝炎”病史，治疗好转后未再复查。“无高血压、冠心病、糖尿病”等病史，“无结核、伤寒”等传染病史，无心、脑、肺、肾等重要脏器疾病史，无外伤史，无手术史,无输血史，无食物过敏史，无药物过敏史,预防接种史不详。;个人史：出生并生长于原籍，久居本地，否认疫水接触史及疫区居留史，居住地无地方病、传染病、流行病流行。居住环境一般，个人卫生习惯一般，无烟、酒嗜好。否认吸毒史，否认冶游史。否认长期毒物及放射性物质接触史。配偶无性病史。;婚育史：已婚已育，1子1女，子女均乙肝病毒携带，爱人体健。;家族史：1哥哥死于“肝肿瘤”，否认家族中有“肺结核、伤寒”等传染病史，否认家族中有“高血压”等家族遗传相关性疾病病史。;体格检查;T：36.4℃；P：86次/分；R:20次/分；BP:139/85mmHg；Wt:50Kg。;发育正常，营养良好，神志清楚，对答切题，自动体位，检体合作。全身皮肤粘膜无明显黄染，未见皮疹及出血点，未见肝掌，未见蜘蛛痣。全身浅表淋巴结未触及肿大。头颅无畸形，五官端正；眼睑无水肿，双眼球运动自如，眼结膜无充血，双侧巩膜无明显黄染，双侧瞳孔等大等圆，对光反射灵敏；耳廓正常，无外耳道异常分泌物，耳突无压痛，听力无障碍，无鼻翼扇动，双鼻腔无异常分泌物，副鼻窦区无压痛。口唇无发绀，口腔粘膜无破溃，口腔气味:正常，牙齿正常，牙龈正常，舌伸舌居中，扁桃体无肿大，咽无充血，声音正常，颈：颈动脉搏动正常，颈动脉杂音无，颈静脉正常，肝颈静脉回流征阴性，气管居中，甲状腺正常，血管杂音无。胸：胸廓对称，无胸骨叩痛，乳房正常。呼吸运动对称，肋间隙正常，呼吸动度一致，呼吸语颤对称，无胸膜摩擦音，双肺叩诊呈清音，肺下界位于锁骨中线第七肋间隙，肺下界移动度6cm，双肺呼吸音清，未闻及干啰音，无胸膜摩擦音，语音传导正常，心前区无隆起，心尖搏动正常，触诊无震颤，心脏相对浊音界正常，心率86次/分，律齐,各瓣膜听诊区未闻及病理性杂音,无心包摩擦音。腹部：体检详见专科检查。脊柱及四肢：脊柱正常，无棘突压痛，活动度正常，四肢活动自如，关节无红肿，双下肢无水肿，无静脉曲张，肌张力正常。神经系统：双膝腱反射对称存在，扑翼样震颤阴性，踝阵挛未引出。;专科检查：神清，全身皮肤粘膜无明显黄染，全身浅表淋巴结未触及肿大；腹平坦，双侧对称，呼吸运动正常，腹壁静脉无曲张，未见胃肠型及肠蠕动波；腹肌柔软，全腹无压痛、反跳痛，未触及肿物及包块，无液波震颤。肝于右锁骨中线肋缘下10cm可触及，边缘顿，无压痛；剑突下3cm可触及；脾于左肋缘下未触及，墨菲氏征阴性，肝上界于右锁骨中线上第五肋间叩出，肝浊音界正常，肝下界位于右肋缘下，肝脾肾区无叩痛，移动性浊音阴性；肠鸣音4次/分，双下肢无水肿。;辅助检查：2020.9.7，我院，AFP 23.8ng/ml，异常凝血酶原 10161 mAU/ml；腹部彩超：肝内多发不均高回声团块或结节（考虑MT）；余肝内声像呈弥漫性病变；3、胆囊壁增厚毛糙；脾肿大。;;，患者的问题为：我的诊断是什么？"
response, history = model.chat(tokenizer, query, history=[])
print(response)