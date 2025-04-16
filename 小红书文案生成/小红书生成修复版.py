"""
小红书文案优化助手
===============================
自动生成符合小红书算法推荐规则的高质量文案
"""

import random
import re
import time
from datetime import datetime

class XiaohongshuContentGenerator:
    def __init__(self):
        # 初始化关键词库
        self.core_keywords = {
            '黑豆/黑豆水': ['黑豆', '黑豆水', '黑色食材', '黑豆煮水', '黑豆茶'],
            '鸡蛋茶': ['鸡蛋茶', '朱雀汤', '打散的鸡蛋', '冲鸡蛋', '鸡蛋花'],
            '问题症状': ['上火', '虚火', '上热下寒', '手脚冰凉', '睡不好', '失眠', '气血不足', 
                    '脾胃不好', '掉发', '口腔溃疡', '便秘', '口干舌燥', '头晕目眩'],
            '功效关键词': ['补气血', '引火下行', '滋阴润燥', '滋阴养性', '健脾胃', '养肾', 
                     '温肾暖胃', '清内热', '养阴安燥'],
            '材料关键词': ['淮山', '山药', '红枣', '红糖', '香油', '白胡椒', '当归', '黄芪', 
                     '枸杞', '桂圆', '莲子', '薏米', '酒酿', '苹果', '赤小豆', '绿豆',
                     '核桃', '黑芝麻', '姜片'],
            '中医理论': ['脾胃为后天之本', '肾为先天之本', '气血生化之源', '阴阳平衡', 
                    '虚不受补', '引火归元', '脾胃不好，百病易生']
        }
        
        # 标签模板
        self.tag_templates = {
            'core': ['养生', '黑豆水', '鸡蛋茶', '朱雀汤', '养生茶'],
            'problem': ['上热下寒', '补气血', '脾胃', '睡眠', '气血不足', '黑色养生食材'],
            'effect': ['引火下行', '健脾胃', '滋阴润燥', '养生日常', '冬藏'],
            'material': ['淮山', '红枣', '当归', '黄芪', '黑豆'],
            'trending': ['养生打卡', '我的养生仪式感', '正式确诊为健康人', '健康养生']
        }
        
        # 文案模板
        self.template_intro = [
            "大家好，我是{年龄}岁的养生博主{博主名}，今天要跟大家分享我坚持喝了{坚持时间}的黑豆鸡蛋茶！",
            "{问题症状}困扰你很久了吗？我曾经也是，直到我发现了这个神奇的黑豆鸡蛋茶配方！",
            "冬天一补就{问题症状}的，一定要喝这个黑豆水鸡蛋茶！今天分享{配方数量}款不同配方！",
            "学养生后才知道，这么多年的黑豆都白吃了！现在教你{配方数量}种正确吃法，解决{问题症状}问题！",
            "如果你经常{问题症状}，不妨试试这个我用了{坚持时间}的黑豆鸡蛋茶，简直太神奇了！"
        ]
        
        self.template_theory = [
            "{中医理论}，黑豆色黑属水，被称为\"肾之骨\"，身体里津液足，{问题症状}自然就能解决。",
            "老话说\"{中医理论}\"，很多人不知道黑豆是天然的养生食材，配上鸡蛋简直就是{功效关键词}的神仙搭配！",
            "中医讲究\"以黑补黑\"，黑豆入肾，鸡蛋滋阴，两者一起煮水{功效关键词}的效果翻倍！",
            "我从{年龄-10}岁开始喝黑豆水，到现在{年龄}岁，{问题症状}的问题完全消失了！关键是方法对！"
        ]
        
        self.template_recipe = [
            "【配方{序号}：{配方名称}】\n\n专治：{问题症状}\n\n材料：\n- 黑豆{黑豆克数}克\n- {材料1}{材料1克数}克\n- {材料2}{材料2克数}克\n- 鸡蛋1个\n- {调味品}\n\n制作：\n1. {步骤1}\n2. {步骤2}\n3. {步骤3}\n4. {步骤4}\n5. {步骤5}\n\n{功效说明}",
        ]
        
        self.template_outro = [
            "【饮用建议】\n\n1. 最佳饮用时间：{饮用时间}\n2. 一周喝{频率}次，不宜天天喝\n3. {注意事项1}\n4. {注意事项2}",
            "坚持喝一个月，你会发现：\n- {效果1}\n- {效果2}\n- {效果3}\n\n{中医理论}，希望这个简单的食疗方子能帮到你！",
            "记住，养生不在于吃多贵的东西，而是找到适合自己的方法！这个成本不到10块钱的黑豆鸡蛋茶，胜过很多昂贵的保健品！"
        ]
        
        # 制作步骤模板
        self.steps_templates = {
            '普通煮法': [
                "将{材料}洗净，加水煮开",
                "转小火煮{时间}分钟（一定要煮透）",
                "碗里打散一个鸡蛋",
                "将煮好的黑豆水沿碗边慢慢倒入，边倒边轻轻搅动",
                "滴几滴香油，撒一点白胡椒粉"
            ],
            '分步煮法': [
                "{材料1}和{材料2}先煮{时间1}分钟",
                "加入{材料3}再煮{时间2}分钟",
                "碗里打散一个鸡蛋",
                "将煮好的汤水沿碗边倒入，形成漩涡冲散鸡蛋",
                "加入{调味品}调味即可"
            ],
            '炒后煮法': [
                "将黑豆小火炒至微微发香（体寒的人适用）",
                "加入{材料}和清水煮开",
                "转小火煮{时间}分钟",
                "将煮好的水冲入打散的鸡蛋中",
                "适量加入{调味品}调味"
            ]
        }
        
        # 效果描述模板
        self.effect_templates = [
            "睡眠更踏实，不再半夜醒来",
            "手脚不再冰凉，气血上升",
            "皮肤状态改善，气色红润",
            "精力充沛，头脑清晰",
            "脸色不黄了，整个气血翻涌",
            "口腔溃疡明显减少",
            "脾胃消化功能增强",
            "大便顺畅，排便规律",
            "掉发量明显减少",
            "眼睛不干涩了，看东西更清晰"
        ]
        
        # 配方名称模板
        self.recipe_names = {
            '黑豆淮山': '经典黑豆淮山鸡蛋茶',
            '黑豆绿豆': '黑豆绿豆清热鸡蛋茶',
            '黑豆赤小豆': '黑豆赤小豆消水肿鸡蛋茶',
            '黑豆苹果': '黑豆苹果养胃鸡蛋茶',
            '黑豆红枣': '黑豆红枣桂圆鸡蛋茶',
            '当归黄芪黑豆': '当归黄芪黑豆鸡蛋茶',
            '黑豆淮山米汤': '黑豆淮山米汤鸡蛋茶',
            '黑豆枸杞': '黑豆枸杞桂圆鸡蛋茶',
            '黑豆醪糟': '黑豆醪糟鸡蛋茶',
            '黑豆核桃': '黑豆核桃分心木鸡蛋茶',
            '黑豆桂皮': '黑豆桂皮姜片鸡蛋茶',
            '黑豆羊肉': '黑豆羊肉温阳鸡蛋茶',
            '黑豆莲子': '黑豆莲子安神鸡蛋茶',
            '黑豆酸枣仁': '黑豆酸枣仁安眠鸡蛋茶',
            '黑豆山药小米': '黑豆山药小米健脾鸡蛋茶',
            '黑豆南瓜': '黑豆南瓜开胃鸡蛋茶',
            '黑豆薏米': '黑豆薏米祛湿鸡蛋茶',
            '黑豆红枣茯苓': '黑豆红枣茯苓养胃鸡蛋茶'
        }
        
        # 饮用时间推荐
        self.drinking_times = [
            "早上空腹", 
            "晚上睡前", 
            "上午9-11点", 
            "下午3-5点", 
            "两餐之间", 
            "姨妈结束后三天内"
        ]
        
        # 注意事项模板
        self.precautions = [
            "经期不建议喝，可以改喝红糖姜茶",
            "喝完半小时内不要吹风、淋雨",
            "黑豆水里的豆子最好不要吃，容易胀气",
            "体质特别寒凉的人可以将黑豆小火炒一下",
            "喝完安静休息，不要看手机",
            "孕妇可以喝，但每次不要超过半碗",
            "不要与寒凉食物一起食用"
        ]
    
    def random_pick(self, items):
        """从列表中随机选择一项"""
        return random.choice(items)
    
    def generate_random_age(self):
        """生成随机年龄，偏向30-45岁"""
        return random.randint(30, 45)
    
    def generate_random_time(self):
        """生成随机坚持时间"""
        units = ["天", "个月", "年"]
        unit = random.choice(units)  # 随机选择一个时间单位
        if unit == "天":
            return f"{random.randint(21, 100)}{unit}"
        elif unit == "个月":
            return f"{random.randint(1, 24)}{unit}"
        else:  # 年
            return f"{random.randint(1, 5)}{unit}"
    
    def generate_random_material_amount(self):
        """生成随机材料用量"""
        return random.randint(10, 25)
    
    def generate_random_cooking_time(self):
        """生成随机烹饪时间"""
        return random.randint(5, 30)
    
    def generate_tags(self, recipe_type, problem_type):
        """生成适合的标签组合"""
        tags = []
        
        # 添加2-3个核心标签
        core_tags = random.sample(self.tag_templates['core'], min(3, len(self.tag_templates['core'])))
        tags.extend(core_tags)
        
        # 添加1-2个问题标签
        problem_tags = random.sample(self.tag_templates['problem'], min(2, len(self.tag_templates['problem'])))
        tags.extend(problem_tags)
        
        # 添加1个功效标签
        effect_tag = random.choice(self.tag_templates['effect'])
        tags.append(effect_tag)
        
        # 添加1个材料标签 - 基于配方类型
        if recipe_type in self.tag_templates['material']:
            tags.append(recipe_type)
        else:
            tags.append(random.choice(self.tag_templates['material']))
        
        # 添加1个流行标签
        trending_tag = random.choice(self.tag_templates['trending'])
        tags.append(trending_tag)
        
        # 确保标签数量不超过8个
        return tags[:8]
    
    def generate_recipe(self, recipe_type, problem_type):
        """生成一个配方"""
        # 确定配方名称
        recipe_name = self.recipe_names.get(recipe_type, f"黑豆{recipe_type}鸡蛋茶")
        
        # 确定材料
        materials = recipe_type.split('黑豆')[-1].strip().split('和')
        if not materials[0]:
            materials = ["淮山", "红枣"]
        
        # 生成材料用量
        material_amounts = [self.generate_random_material_amount() for _ in range(len(materials))]
        
        # 随机选择一种调味品
        seasoning = random.choice(["香油几滴和白胡椒粉少许", "少量蜂蜜", "红糖适量", "少量海盐", "冰糖适量"])
        
        # 随机选择一种步骤模板
        step_template = self.random_pick(list(self.steps_templates.keys()))
        steps = self.steps_templates[step_template]
        
        # 替换步骤中的占位符
        updated_steps = []
        for step in steps:
            updated_step = step
            if "{材料}" in step:
                updated_step = updated_step.replace("{材料}", "、".join(materials))
            if "{材料1}" in step and len(materials) > 0:
                updated_step = updated_step.replace("{材料1}", materials[0])
            if "{材料2}" in step and len(materials) > 1:
                updated_step = updated_step.replace("{材料2}", materials[1])
            if "{材料3}" in step and len(materials) > 2:
                updated_step = updated_step.replace("{材料3}", materials[2] if len(materials) > 2 else "适量姜片")
            if "{时间}" in step:
                updated_step = updated_step.replace("{时间}", str(self.generate_random_cooking_time()))
            if "{时间1}" in step:
                updated_step = updated_step.replace("{时间1}", str(self.generate_random_cooking_time()))
            if "{时间2}" in step:
                updated_step = updated_step.replace("{时间2}", str(self.generate_random_cooking_time()))
            if "{调味品}" in step:
                updated_step = updated_step.replace("{调味品}", seasoning.split("和")[0])
            
            updated_steps.append(updated_step)
        
        # 生成功效说明
        effect = f"这款特别适合{problem_type}的人，{self.random_pick(self.core_keywords['功效关键词'])}效果明显，喝完{self.random_pick(self.effect_templates).lower()}。"
        
        # 组装配方
        recipe = {
            "名称": recipe_name,
            "针对问题": problem_type,
            "材料": ["黑豆"] + materials,
            "材料用量": [15] + material_amounts,
            "调味品": seasoning,
            "步骤": updated_steps,
            "功效": effect
        }
        
        return recipe
    
    def generate_title(self, problem_type, recipe_types):
        """生成文章标题"""
        title_templates = [
            "从{问题症状}到气色翻涌！{数量}款黑豆鸡蛋茶配方大公开",
            "黑豆还有这个妙用？{数量}款配方专治{问题症状}",
            "{问题症状}终于好了！{数量}天喝黑豆鸡蛋茶的惊人变化",
            "解锁黑豆{数量}种吃法，专治{问题症状}不上火",
            "不花一分冤枉钱！自制黑豆鸡蛋茶{数量}款配方治愈{问题症状}",
            "{数量}款黑豆鸡蛋茶配方|坚持一个月{问题症状}竟然消失了！",
            "学养生后才知道，黑豆原来可以这样吃！{数量}种配方解决{问题症状}"
        ]
        
        template = self.random_pick(title_templates)
        title = template.replace("{问题症状}", problem_type).replace("{数量}", str(len(recipe_types)))
        
        return title 
    
    def generate_full_content(self, problem_type, recipe_types=None, blogger_name=None):
        """生成完整的文章内容"""
        if blogger_name is None:
            blogger_names = ["小七", "芊芊", "苗苗", "小叶", "小瑜", "香香姐", "小厨"]
            blogger_name = self.random_pick(blogger_names)
        
        if recipe_types is None:
            # 随机选择3-5个配方类型
            all_recipe_types = list(self.recipe_names.keys())
            recipe_count = random.randint(3, 5)
            recipe_types = random.sample(all_recipe_types, recipe_count)
        
        # 生成基本变量
        age = self.generate_random_age()
        persistence_time = self.generate_random_time()
        recipe_count = len(recipe_types)
        
        # 生成标题
        title = self.generate_title(problem_type, recipe_types)
        
        # 生成标签
        tags = self.generate_tags(recipe_types[0].split('黑豆')[-1], problem_type)
        tags_text = " ".join([f"#{tag}" for tag in tags])
        
        # 生成引言
        intro_template = self.random_pick(self.template_intro)
        intro = intro_template.replace("{年龄}", str(age)) \
                             .replace("{博主名}", blogger_name) \
                             .replace("{坚持时间}", persistence_time) \
                             .replace("{问题症状}", problem_type) \
                             .replace("{配方数量}", str(recipe_count))
        
        # 生成理论解释部分
        theory_template = self.random_pick(self.template_theory)
        theory = theory_template.replace("{中医理论}", self.random_pick(self.core_keywords['中医理论'])) \
                               .replace("{问题症状}", problem_type) \
                               .replace("{功效关键词}", self.random_pick(self.core_keywords['功效关键词'])) \
                               .replace("{年龄}", str(age)) \
                               .replace("{年龄-10}", str(age-10))
        
        # 生成每个配方
        recipes_content = ""
        for i, recipe_type in enumerate(recipe_types):
            recipe = self.generate_recipe(recipe_type, problem_type)
            
            recipe_template = self.template_recipe[0]
            recipe_content = recipe_template.replace("{序号}", str(i+1)) \
                                           .replace("{配方名称}", recipe["名称"]) \
                                           .replace("{问题症状}", recipe["针对问题"]) \
                                           .replace("{黑豆克数}", str(recipe["材料用量"][0])) \
                                           .replace("{材料1}", recipe["材料"][1] if len(recipe["材料"]) > 1 else "") \
                                           .replace("{材料1克数}", str(recipe["材料用量"][1]) if len(recipe["材料用量"]) > 1 else "") \
                                           .replace("{材料2}", recipe["材料"][2] if len(recipe["材料"]) > 2 else "") \
                                           .replace("{材料2克数}", str(recipe["材料用量"][2]) if len(recipe["材料用量"]) > 2 else "") \
                                           .replace("{调味品}", recipe["调味品"]) \
                                           .replace("{步骤1}", recipe["步骤"][0]) \
                                           .replace("{步骤2}", recipe["步骤"][1]) \
                                           .replace("{步骤3}", recipe["步骤"][2]) \
                                           .replace("{步骤4}", recipe["步骤"][3]) \
                                           .replace("{步骤5}", recipe["步骤"][4] if len(recipe["步骤"]) > 4 else "搅拌均匀即可食用") \
                                           .replace("{功效说明}", recipe["功效"])
            
            recipes_content += recipe_content + "\n\n"
        
        # 生成结语
        outro_template = self.random_pick(self.template_outro)
        # 先获取随机的注意事项1
        注意事项1 = self.random_pick(self.precautions)
        # 然后获取与注意事项1不同的注意事项2
        注意事项2 = self.random_pick([p for p in self.precautions if p != 注意事项1])
        # 获取随机效果
        效果1 = self.random_pick(self.effect_templates)
        效果2 = self.random_pick([e for e in self.effect_templates if e != 效果1])
        效果3 = self.random_pick([e for e in self.effect_templates if e not in [效果1, 效果2]])
        
        outro = outro_template.replace("{饮用时间}", self.random_pick(self.drinking_times)) \
                             .replace("{频率}", str(random.randint(3, 5))) \
                             .replace("{注意事项1}", 注意事项1) \
                             .replace("{注意事项2}", 注意事项2) \
                             .replace("{效果1}", 效果1) \
                             .replace("{效果2}", 效果2) \
                             .replace("{效果3}", 效果3) \
                             .replace("{中医理论}", self.random_pick(self.core_keywords['中医理论']))
        
        # 组装完整内容
        full_content = f"{title}\n\n{tags_text}\n\n{intro}\n\n{theory}\n\n{recipes_content}{outro}\n\n我是{blogger_name}，关注我，教你更多不花冤枉钱的养生小妙招！"
        
        return {
            "title": title,
            "tags": tags,
            "content": full_content,
            "problem_type": problem_type,
            "recipe_types": recipe_types,
            "blogger_name": blogger_name
        }
    
    def generate_content_by_problem(self, problem_type):
        """根据特定问题生成内容"""
        # 根据问题类型选择合适的配方类型
        recipe_mapping = {
            "上火": ["黑豆绿豆", "黑豆淮山", "黑豆苹果"],
            "虚火": ["黑豆淮山", "黑豆赤小豆", "黑豆红枣"],
            "上热下寒": ["黑豆桂皮", "黑豆羊肉", "黑豆淮山"],
            "手脚冰凉": ["黑豆桂皮", "黑豆醪糟", "黑豆羊肉"],
            "睡不好": ["黑豆莲子", "黑豆酸枣仁", "黑豆红枣"],
            "失眠": ["黑豆酸枣仁", "黑豆红枣", "黑豆莲子"],
            "气血不足": ["当归黄芪黑豆", "黑豆枸杞", "黑豆红枣"],
            "脾胃不好": ["黑豆山药小米", "黑豆淮山米汤", "黑豆南瓜"],
            "掉发": ["黑豆核桃", "黑豆枸杞", "当归黄芪黑豆"],
            "口腔溃疡": ["黑豆绿豆", "黑豆淮山", "黑豆赤小豆"],
            "便秘": ["黑豆薏米", "黑豆赤小豆", "黑豆南瓜"],
            "口干舌燥": ["黑豆淮山", "黑豆苹果", "黑豆绿豆"],
            "头晕目眩": ["当归黄芪黑豆", "黑豆枸杞", "黑豆红枣桂圆"]
        }
        
        # 如果没有直接匹配，选择一些通用配方
        default_recipes = ["黑豆淮山", "黑豆红枣", "黑豆醪糟"]
        
        # 获取适合这个问题的配方或使用默认配方
        recipes = recipe_mapping.get(problem_type, default_recipes)
        
        # 生成内容
        return self.generate_full_content(problem_type, recipes)
    
    def optimize_existing_content(self, content):
        """优化现有内容，提高关键词密度和相似度"""
        # 分析当前内容
        current_keywords = {}
        for category, keywords in self.core_keywords.items():
            for keyword in keywords:
                count = content.count(keyword)
                if count > 0:
                    current_keywords[keyword] = count
        
        # 计算当前关键词总数
        total_keywords = sum(current_keywords.values())
        content_length = len(content)
        
        # 如果关键词密度不足，增加关键词
        target_keywords = 15  # 目标关键词数量
        if total_keywords < target_keywords:
            # 需要添加的关键词数量
            to_add = target_keywords - total_keywords
            
            # 选择一些关键词进行添加
            missing_keywords = []
            for category, keywords in self.core_keywords.items():
                for keyword in keywords:
                    if keyword not in current_keywords or current_keywords[keyword] < 2:
                        missing_keywords.append(keyword)
            
            # 如果有缺失的关键词，随机选择一些进行添加
            if missing_keywords:
                selected_keywords = random.sample(missing_keywords, min(to_add, len(missing_keywords)))
                
                # 构建增强内容
                enhanced_content = content
                for keyword in selected_keywords:
                    # 随机生成一个包含该关键词的短语
                    phrases = [
                        f"记住，{keyword}是非常重要的。",
                        f"不要忘记{keyword}的神奇作用。",
                        f"{keyword}的效果真的很显著。",
                        f"很多人不知道{keyword}的重要性。"
                    ]
                    phrase = random.choice(phrases)
                    
                    # 将短语插入内容的随机位置
                    insert_pos = random.randint(content_length // 3, content_length * 2 // 3)
                    enhanced_content = enhanced_content[:insert_pos] + " " + phrase + " " + enhanced_content[insert_pos:]
                
                return enhanced_content
        
        # 如果关键词密度已经足够，返回原内容
        return content

def interactive_app():
    """交互式应用程序"""
    generator = XiaohongshuContentGenerator()
    
    print("\n================================")
    print("  小红书文案优化助手 v1.0")
    print("================================\n")
    
    while True:
        print("\n【主菜单】")
        print("1. 生成新文案")
        print("2. 优化现有文案")
        print("3. 分析文案数据")
        print("4. 垂类迁移工具")
        print("5. 退出")
        
        choice = input("\n请选择功能(1-5): ")
        
        if choice == '1':
            # 生成新文案
            print("\n【生成新文案】")
            print("\n可选问题症状:")
            problem_types = generator.core_keywords['问题症状']
            for i, problem in enumerate(problem_types):
                print(f"{i+1}. {problem}")
            
            try:
                problem_index = int(input("\n请选择问题症状编号: ")) - 1
                if 0 <= problem_index < len(problem_types):
                    problem_type = problem_types[problem_index]
                    print(f"\n正在生成针对「{problem_type}」的文案...")
                    time.sleep(1)  # 模拟生成延迟
                    result = generator.generate_content_by_problem(problem_type)
                    
                    print("\n============= 生成结果 =============\n")
                    print(f"标题: {result['title']}")
                    print(f"标签: {' '.join(['#'+tag for tag in result['tags']])}")
                    print("\n------- 正文 -------\n")
                    print(result['content'])
                    print("\n=================================\n")
                    
                    save = input("是否保存到文件? (y/n): ")
                    if save.lower() == 'y':
                        filename = f"小红书_{problem_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                        with open(filename, 'w', encoding='utf-8') as f:
                            f.write(result['content'])
                        print(f"已保存到文件: {filename}")
                else:
                    print("无效的选择，请重试。")
            except ValueError:
                print("请输入有效的数字。")
        
        elif choice == '2':
            # 优化现有文案
            print("\n【优化现有文案】")
            filename = input("请输入文案文件名或直接粘贴文案内容: ")
            
            content = ""
            if os.path.exists(filename):
                try:
                    with open(filename, 'r', encoding='utf-8') as f:
                        content = f.read()
                except:
                    print("读取文件失败，请确认文件路径正确。")
            else:
                content = filename  # 假设用户直接粘贴了内容
            
            if content:
                print("\n正在优化文案...")
                time.sleep(1.5)  # 模拟处理时间
                optimized = generator.optimize_existing_content(content)
                
                print("\n============= 优化结果 =============\n")
                print(optimized)
                print("\n=================================\n")
                
                save = input("是否保存优化后的文案? (y/n): ")
                if save.lower() == 'y':
                    save_filename = f"优化_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                    with open(save_filename, 'w', encoding='utf-8') as f:
                        f.write(optimized)
                    print(f"已保存到文件: {save_filename}")
        
        elif choice == '3':
            print("\n【分析文案数据】功能开发中...")
            # 这里可以实现文案数据分析功能
            
        elif choice == '4':
            print("\n【垂类迁移工具】功能开发中...")
            # 这里可以实现垂类迁移功能
            
        elif choice == '5':
            print("\n感谢使用小红书文案优化助手！再见！")
            break
            
        else:
            print("无效的选择，请输入1-5之间的数字。")
        
        input("\n按Enter键继续...")

# 添加主函数执行入口
if __name__ == "__main__":
    import os
    interactive_app() 