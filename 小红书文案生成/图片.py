import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors
from matplotlib.path import Path
import matplotlib.patheffects as path_effects
import matplotlib.cm as cm
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.font_manager as fm

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS', 'SimSun', 'DejaVu Sans']  # 优先使用黑体，然后是微软雅黑
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
plt.rcParams['font.family'] = 'sans-serif'

# 尝试查找系统中可用的中文字体
fonts = [f.name for f in fm.fontManager.ttflist]
chinese_fonts = [f for f in fonts if any(name in f for name in ['SimHei', 'Microsoft YaHei', '微软雅黑', '黑体', 'SimSun', '宋体'])]
if chinese_fonts:
    plt.rcParams['font.sans-serif'] = chinese_fonts + plt.rcParams['font.sans-serif']
    print(f"找到可用的中文字体: {chinese_fonts}")
else:
    print("警告: 未找到中文字体，图表中文可能显示为方块")

# Initialize image title list
_mfajlsdf98q21_image_title_list = []

# Define custom colors
gold_color = '#D4AF37'
white_color = '#FFFFFF'
earth_yellow = '#E1C16E'
beige_color = '#F5F5DC'
sand_color = '#C2B280'

# Create a custom colormap with gold and earth tones
colors = [(1, 1, 1), (0.83, 0.69, 0.43), (0.76, 0.49, 0.05)]  # white to earth yellow to gold
custom_cmap = LinearSegmentedColormap.from_list('gold_earth', colors, N=100)

# Sample data for xiaohongshu black bean egg tea content
features = [
    "黑豆配方多样性", "中医理论引用", "个人故事", "具体做法详细度", 
    "功效描述", "标题吸引力", "搭配食材新鲜度", "标签数量", 
    "重点人群定位", "图文质量"
]

# Importance scores based on our analysis
importance_scores = [0.85, 0.78, 0.92, 0.76, 0.89, 0.95, 0.82, 0.71, 0.87, 0.79]

# 1. Simplified Decision Tree for Black Bean Egg Tea Content Recommendation
plt.figure(figsize=(14, 10))
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

# Set background color
ax = plt.gca()
ax.set_facecolor(beige_color)
plt.gcf().set_facecolor(white_color)

# Draw the tree nodes
def draw_node(x, y, width, height, label, level=0, is_leaf=False):
    colors = [white_color, earth_yellow, gold_color]
    color = colors[min(level, len(colors) - 1)]
    
    rect = plt.Rectangle((x - width/2, y - height/2), width, height, 
                        facecolor=color, edgecolor='black', alpha=0.8,
                        linewidth=2, zorder=2)
    ax.add_patch(rect)
    
    text = plt.text(x, y, label, ha='center', va='center', fontsize=11, 
                   fontweight='bold', color='black', zorder=3)
    text.set_path_effects([path_effects.withStroke(linewidth=3, foreground=color)])

# Draw connections between nodes
def draw_connection(x1, y1, x2, y2, label=''):
    plt.plot([x1, x2], [y1, y2], 'k-', linewidth=2, alpha=0.7, zorder=1)
    
    if label:
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        plt.text(mid_x, mid_y, label, ha='center', va='center', 
                fontsize=10, backgroundcolor=beige_color)

# Tree structure
# Root
draw_node(7, 9, 4, 1, "小红书黑豆鸡蛋茶内容")

# Level 1
draw_node(3.5, 7, 3, 0.8, "内容主题特征", 1)
draw_node(10.5, 7, 3, 0.8, "表现形式特征", 1)

# Level 2 - left branch
draw_node(2, 5, 2, 0.8, "理论支撑", 2)
draw_node(5, 5, 2, 0.8, "功效定位", 2)

# Level 2 - right branch
draw_node(8.5, 5, 2, 0.8, "故事性", 2)
draw_node(12.5, 5, 2, 0.8, "标题/标签", 2)

# Level 3 - leaves
draw_node(1, 3, 1.8, 0.8, "中医理论引用", 2, True)
draw_node(3, 3, 1.8, 0.8, "配方多样性", 2, True)
draw_node(4.5, 3, 1.8, 0.8, "针对问题", 2, True)
draw_node(6.5, 3, 1.8, 0.8, "人群定位", 2, True)
draw_node(8, 3, 1.8, 0.8, "个人体验", 2, True)
draw_node(10, 3, 1.8, 0.8, "前后对比", 2, True)
draw_node(11.5, 3, 1.8, 0.8, "标题吸引力", 2, True)
draw_node(13.5, 3, 1.8, 0.8, "标签覆盖度", 2, True)

# Draw connections
draw_connection(7, 9, 3.5, 7, "内容特征")
draw_connection(7, 9, 10.5, 7, "形式特征")

draw_connection(3.5, 7, 2, 5, "知识维度")
draw_connection(3.5, 7, 5, 5, "应用维度")
draw_connection(10.5, 7, 8.5, 5, "情感共鸣")
draw_connection(10.5, 7, 12.5, 5, "曝光能力")

# Connect to leaves
draw_connection(2, 5, 1, 3)
draw_connection(2, 5, 3, 3)
draw_connection(5, 5, 4.5, 3)
draw_connection(5, 5, 6.5, 3)
draw_connection(8.5, 5, 8, 3)
draw_connection(8.5, 5, 10, 3)
draw_connection(12.5, 5, 11.5, 3)
draw_connection(12.5, 5, 13.5, 3)

plt.title('小红书黑豆鸡蛋茶内容推荐决策树', fontsize=16, color='black', 
         fontweight='bold', pad=20)
plt.axis('off')

_mfajlsdf98q21_image_title_list.append("Simplified Decision Tree for Black Bean Egg Tea Content Recommendation")
plt.show()

# 2. Feature Importance Bar Chart
plt.figure(figsize=(14, 10))
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.3)

# Set background color
ax = plt.gca()
ax.set_facecolor(beige_color)
plt.gcf().set_facecolor(white_color)

# Create horizontal bar chart
bars = plt.barh(features, importance_scores, color=gold_color, alpha=0.8, 
             edgecolor='black', linewidth=1.5)

# Add value labels to the bars
for i, bar in enumerate(bars):
    plt.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height()/2, 
            f'{importance_scores[i]:.2f}', va='center', fontweight='bold')

# Add a vertical line for average importance
avg_importance = np.mean(importance_scores)
plt.axvline(x=avg_importance, color='black', linestyle='--', 
          linewidth=2, alpha=0.7)
plt.text(avg_importance + 0.01, -0.5, f'Average: {avg_importance:.2f}', 
       fontsize=10, va='center')

# Customize plot
plt.xlim(0, 1.1)
plt.title('小红书黑豆鸡蛋茶内容特征重要性分析', fontsize=16, 
        color='black', fontweight='bold', pad=20)
plt.xlabel('重要性得分', fontsize=14, color='black', fontweight='bold')
plt.ylabel('内容特征', fontsize=14, color='black', fontweight='bold')
plt.grid(axis='x', linestyle='--', alpha=0.3)

for spine in ax.spines.values():
    spine.set_color(gold_color)
    spine.set_linewidth(2)

_mfajlsdf98q21_image_title_list.append("Feature Importance Analysis for Black Bean Egg Tea Content")
plt.show()

# 3. Content Recommendation Simplified Flow Chart
plt.figure(figsize=(14, 10))
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

# Set background color
ax = plt.gca()
ax.set_facecolor(beige_color)
plt.gcf().set_facecolor(white_color)

# Define the positions of the boxes
positions = {
    'content': (5, 8),
    'engagement': (5, 6),
    'similarity': (2, 4),
    'keywords': (5, 4),
    'emotion': (8, 4),
    'theme': (2, 2),
    'format': (5, 2),
    'timing': (8, 2),
    'recommendation': (5, 0)
}

# Define box sizes
box_width = 2.5
box_height = 1

# Function to draw boxes and arrows
def draw_box(key, label, level=0):
    x, y = positions[key]
    colors = [white_color, earth_yellow, gold_color]
    color = colors[min(level, len(colors) - 1)]
    
    rect = plt.Rectangle((x - box_width/2, y - box_height/2), box_width, box_height, 
                       facecolor=color, edgecolor='black', alpha=0.8,
                       linewidth=2, zorder=2)
    ax.add_patch(rect)
    
    text = plt.text(x, y, label, ha='center', va='center', fontsize=12, 
                  fontweight='bold', color='black', zorder=3)
    text.set_path_effects([path_effects.withStroke(linewidth=3, foreground=color)])

def draw_arrow(start_key, end_key, label=''):
    start_x, start_y = positions[start_key]
    end_x, end_y = positions[end_key]
    
    # Calculate start and end points to be at the edge of the boxes
    if start_y > end_y:  # Arrow going down
        start_y -= box_height/2
        end_y += box_height/2
    elif start_y < end_y:  # Arrow going up
        start_y += box_height/2
        end_y -= box_height/2
    
    if start_x > end_x:  # Arrow going left
        start_x -= box_width/2
        end_x += box_width/2
    elif start_x < end_x:  # Arrow going right
        start_x += box_width/2
        end_x -= box_width/2
        
    plt.arrow(start_x, start_y, end_x - start_x, end_y - start_y, 
            head_width=0.2, head_length=0.3, fc='black', ec='black', 
            length_includes_head=True, zorder=1, alpha=0.7)
    
    if label:
        mid_x = (start_x + end_x) / 2
        mid_y = (start_y + end_y) / 2
        plt.text(mid_x, mid_y, label, ha='center', va='center', 
               fontsize=10, backgroundcolor=beige_color, zorder=3)

# Draw boxes
draw_box('content', '养生内容创作', 0)
draw_box('engagement', '用户互动分析', 0)
draw_box('similarity', '相似度计算', 1)
draw_box('keywords', '关键词权重', 1)
draw_box('emotion', '情感价值评估', 1)
draw_box('theme', '主题聚类', 2)
draw_box('format', '内容形式优化', 2)
draw_box('timing', '发布时机选择', 2)
draw_box('recommendation', '算法推荐流量分配', 2)

# Draw arrows
draw_arrow('content', 'engagement', '内容发布')
draw_arrow('engagement', 'similarity', '相似内容分析')
draw_arrow('engagement', 'keywords', '关键词提取')
draw_arrow('engagement', 'emotion', '情感反应分析')
draw_arrow('similarity', 'theme', '同类主题归纳')
draw_arrow('keywords', 'format', '关键要素提炼')
draw_arrow('emotion', 'timing', '情感共鸣时机')
draw_arrow('theme', 'recommendation', '主题权重')
draw_arrow('format', 'recommendation', '形式评分')
draw_arrow('timing', 'recommendation', '时机适配度')

plt.title('小红书内容推荐算法流程简化图', fontsize=16, 
        color='black', fontweight='bold', pad=20)
plt.axis('off')

_mfajlsdf98q21_image_title_list.append("Simplified Content Recommendation Algorithm Flow Chart")
plt.show()

# 4. Algorithm Applicability Analysis for Different Vertical Categories
plt.figure(figsize=(14, 10))
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

# Set background color
ax = plt.gca()
ax.set_facecolor(beige_color)
plt.gcf().set_facecolor(white_color)

# Define categories and their scores for different algorithm components
categories = ['养生饮食', '美妆护肤', '旅游分享', '家居装饰', '母婴育儿', '数码评测', '穿搭时尚']
algorithm_components = ['关键词密度', '标签优化', '故事性展示', '专业术语', '实操指南', '个人体验']

# Scores for each category and component (higher is better applicability)
scores = np.array([
    [0.95, 0.85, 0.90, 0.90, 0.95, 0.85],  # 养生饮食
    [0.80, 0.95, 0.85, 0.75, 0.90, 0.95],  # 美妆护肤
    [0.70, 0.85, 0.95, 0.60, 0.75, 0.95],  # 旅游分享
    [0.75, 0.80, 0.85, 0.65, 0.90, 0.80],  # 家居装饰
    [0.85, 0.90, 0.90, 0.80, 0.95, 0.90],  # 母婴育儿
    [0.65, 0.70, 0.75, 0.95, 0.90, 0.85],  # 数码评测
    [0.70, 0.95, 0.80, 0.60, 0.75, 0.90],  # 穿搭时尚
])

# Create a heatmap
plt.imshow(scores, cmap=custom_cmap, aspect='auto', alpha=0.8)

# Add text annotations
for i in range(len(categories)):
    for j in range(len(algorithm_components)):
        text = plt.text(j, i, f'{scores[i, j]:.2f}', ha='center', va='center', 
                      color='black', fontweight='bold')

# Add category effectiveness score (row average)
category_avg = np.mean(scores, axis=1)
for i, avg in enumerate(category_avg):
    plt.text(len(algorithm_components), i, f'{avg:.2f}', ha='center', va='center',
           color='black', fontweight='bold', backgroundcolor=gold_color)

# Add component versatility score (column average)
component_avg = np.mean(scores, axis=0)
for j, avg in enumerate(component_avg):
    plt.text(j, len(categories), f'{avg:.2f}', ha='center', va='center',
           color='black', fontweight='bold', backgroundcolor=gold_color)

# Overall adaptability score
overall_avg = np.mean(scores)
plt.text(len(algorithm_components), len(categories), f'{overall_avg:.2f}', 
       ha='center', va='center', color='black', fontweight='bold', 
       backgroundcolor=gold_color)

# Set axis ticks and labels
plt.xticks(np.arange(len(algorithm_components)), algorithm_components, rotation=45, ha='right')
plt.yticks(np.arange(len(categories)), categories)

# Add an extra column and row for averages
plt.xticks(np.arange(len(algorithm_components) + 1), 
         algorithm_components + ['有效性均值'], rotation=45, ha='right')
plt.yticks(np.arange(len(categories) + 1), 
         categories + ['通用性均值'])

# Add colorbar
cbar = plt.colorbar(shrink=0.8)
cbar.set_label('算法适用度评分', rotation=270, labelpad=20, fontweight='bold')

# Customize plot
plt.title('小红书算法机制在不同垂类应用适配性分析', fontsize=16, 
        color='black', fontweight='bold', pad=20)
plt.tight_layout()

for spine in ax.spines.values():
    spine.set_color(gold_color)
    spine.set_linewidth(2)

_mfajlsdf98q21_image_title_list.append("Algorithm Applicability Analysis for Different Vertical Categories")
plt.show()

#@mf:requirement:matplotlib
#@mf:requirement:numpy