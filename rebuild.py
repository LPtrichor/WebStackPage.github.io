#!/usr/bin/env python3
"""
爆改 WebStackPage 为 AI 导航站 - 完整版
"""
import os

NAV_CATEGORIES = [
    {
        "icon": "linecons-star",
        "id": "热门AI",
        "title": "热门 AI",
        "items": [
            {"name": "ChatGPT", "url": "https://chatgpt.com", "desc": "OpenAI 旗下最强 AI 助手，GPT-5.5 模型"},
            {"name": "Claude", "url": "https://claude.ai", "desc": "Anthropic 出品，长文本和编程能力顶尖"},
            {"name": "Gemini", "url": "https://gemini.google.com", "desc": "Google 多模态 AI，深度集成 Google 全家桶"},
            {"name": "Perplexity", "url": "https://www.perplexity.ai", "desc": "AI 搜索引擎，带引用来源的精准回答"},
            {"name": "Grok", "url": "https://grok.xai.com", "desc": "马斯克旗下 xAI，实时数据+图像生成"},
            {"name": "通义千问", "url": "https://tongyi.aliyun.com", "desc": "阿里出品，中文理解能力最强的大模型"},
            {"name": "文心一言", "url": "https://yiyan.baidu.com", "desc": "百度大模型，适合中文创作和办公"},
            {"name": "Kimi", "url": "https://kimi.moonshot.cn", "desc": "月之暗面出品，超长文本阅读助手"},
        ]
    },
    {
        "icon": "linecons-code",
        "id": "AI编程",
        "title": "AI 编程",
        "items": [
            {"name": "Cursor", "url": "https://cursor.com", "desc": "AI 原生代码编辑器，2026 年最火编程工具"},
            {"name": "Claude Code", "url": "https://claude.ai/code", "desc": "Anthropic 的终端 AI 编程助手"},
            {"name": "GitHub Copilot", "url": "https://github.com/features/copilot", "desc": "GitHub 官方 AI 代码补全，IDE 内无缝使用"},
            {"name": "Trae", "url": "https://www.trae.ai", "desc": "字节跳动出品，免费 AI 编程 IDE"},
            {"name": "Windsurf", "url": "https://windsurf.com", "desc": "Codeium 出品的 AI 编程编辑器"},
            {"name": "Devin", "url": "https://devin.ai", "desc": "Cognition 的自主 AI 工程师"},
            {"name": "Bolt.new", "url": "https://bolt.new", "desc": "浏览器内 AI 全栈开发，秒级创建应用"},
            {"name": "v0.dev", "url": "https://v0.dev", "desc": "Vercel AI 前端生成器，一句话生成 UI"},
        ]
    },
    {
        "icon": "linecons-camera",
        "id": "AI绘画",
        "title": "AI 绘画",
        "items": [
            {"name": "Midjourney", "url": "https://www.midjourney.com", "desc": "最强 AI 绘画，艺术感和细节无人能敌"},
            {"name": "DALL·E 3", "url": "https://chatgpt.com", "desc": "OpenAI 图像生成，ChatGPT 内直接使用"},
            {"name": "Flux", "url": "https://blackforestlabs.ai", "desc": "开源最强图像生成模型，效果惊艳"},
            {"name": "Stable Diffusion", "url": "https://stability.ai", "desc": "开源 AI 绘画标杆，可本地部署"},
            {"name": "Ideogram", "url": "https://ideogram.ai", "desc": "AI 文字排版+图像生成，设计海报利器"},
            {"name": "SeaArt", "url": "https://www.seaart.ai", "desc": "免费 AI 绘画平台，支持多种模型"},
            {"name": "LiblibAI", "url": "https://www.liblib.art", "desc": "国内最大 AI 绘画模型分享社区"},
            {"name": "Nijijourney", "url": "https://nijijourney.com", "desc": "Midjourney 动漫风格专版，二次元首选"},
        ]
    },
    {
        "icon": "linecons-video",
        "id": "AI视频",
        "title": "AI 视频",
        "items": [
            {"name": "Kling 可灵", "url": "https://klingai.com", "desc": "快手出品，AI 视频生成国内最强"},
            {"name": "Veo 3", "url": "https://labs.google", "desc": "Google 最新视频生成模型，720p 高质量"},
            {"name": "Runway Gen-4", "url": "https://runwayml.com", "desc": "AI 视频生成先驱，专业级视频编辑"},
            {"name": "Pika", "url": "https://pika.art", "desc": "AI 视频生成+编辑，操作简单效果好"},
            {"name": "Luma Dream Machine", "url": "https://lumalabs.ai", "desc": "高质量 AI 视频生成，支持图生视频"},
            {"name": "MiniMax 海螺", "url": "https://hailuoai.com", "desc": "MiniMax 视频生成模型，中文理解优秀"},
            {"name": "Sora", "url": "https://sora.com", "desc": "OpenAI 视频生成，已集成 ChatGPT"},
            {"name": "剪映 AI", "url": "https://www.capcut.cn", "desc": "字节旗下，AI 剪辑+字幕+配音一站式"},
        ]
    },
    {
        "icon": "linecons-music",
        "id": "AI音频",
        "title": "AI 音频",
        "items": [
            {"name": "Suno", "url": "https://suno.com", "desc": "AI 音乐生成，一句话创作完整歌曲"},
            {"name": "Udio", "url": "https://www.udio.com", "desc": "高质量 AI 音乐生成，音质和编曲出色"},
            {"name": "ElevenLabs", "url": "https://elevenlabs.io", "desc": "AI 语音合成，最逼真的人声克隆"},
            {"name": "Fish Audio", "url": "https://fish.audio", "desc": "开源 AI 语音合成，支持多语言"},
            {"name": "Adobe Podcast", "url": "https://podcast.adobe.com", "desc": "AI 音频增强，一键降噪+提升音质"},
            {"name": "Whisper", "url": "https://openai.com/index/whisper", "desc": "OpenAI 语音转文字，多语言高精度"},
        ]
    },
    {
        "icon": "linecons-search",
        "id": "AI搜索",
        "title": "AI 搜索",
        "items": [
            {"name": "Perplexity", "url": "https://www.perplexity.ai", "desc": "AI 搜索引擎，带引用来源"},
            {"name": "秘塔 AI 搜索", "url": "https://metaso.cn", "desc": "国内最好用的 AI 搜索引擎"},
            {"name": "天工 AI", "url": "https://www.tiangong.cn", "desc": "昆仑万维 AI 搜索+创作平台"},
            {"name": "纳米 AI 搜索", "url": "https://www.n.cn", "desc": "360 旗下 AI 搜索，中文能力强"},
            {"name": "Google AI Overviews", "url": "https://www.google.com", "desc": "Google 搜索结果中的 AI 摘要"},
            {"name": "You.com", "url": "https://you.com", "desc": "隐私优先的 AI 搜索引擎"},
        ]
    },
    {
        "icon": "linecons-pencil",
        "id": "AI写作",
        "title": "AI 写作",
        "items": [
            {"name": "Notion AI", "url": "https://www.notion.so", "desc": "笔记+AI 写作，知识管理神器"},
            {"name": "Jasper", "url": "https://www.jasper.ai", "desc": "AI 营销文案生成，品牌内容利器"},
            {"name": "Grammarly", "url": "https://www.grammarly.com", "desc": "AI 英文语法检查和写作优化"},
            {"name": "火山写作", "url": "https://www.writingo.net", "desc": "字节旗下 AI 写作助手，中英文双语"},
            {"name": "笔灵 AI", "url": "https://ibiling.cn", "desc": "国内 AI 写作工具，支持多种文体"},
            {"name": "WPS AI", "url": "https://www.wps.cn", "desc": "金山办公 AI，Word/PPT 智能助手"},
        ]
    },
    {
        "icon": "linecons-diamond",
        "id": "AI工具",
        "title": "AI 工具",
        "items": [
            {"name": "n8n", "url": "https://n8n.io", "desc": "开源 AI 工作流自动化平台"},
            {"name": "Dify", "url": "https://dify.ai", "desc": "开源 LLM 应用开发平台"},
            {"name": "Coze", "url": "https://www.coze.cn", "desc": "字节 AI 应用开发平台，零代码创建 Bot"},
            {"name": "Make", "url": "https://www.make.com", "desc": "可视化自动化工作流，连接 1500+ 应用"},
            {"name": "Zapier", "url": "https://zapier.com", "desc": "老牌自动化工具，AI 功能日益强大"},
            {"name": "HuggingFace", "url": "https://huggingface.co", "desc": "AI 模型托管平台，开源社区大本营"},
        ]
    },
    {
        "icon": "linecons-graduation-cap",
        "id": "AI学习",
        "title": "AI 学习",
        "items": [
            {"name": "AI 前线", "url": "https://www.infoq.cn/ai", "desc": "InfoQ AI 频道，前沿技术深度解读"},
            {"name": "机器之心", "url": "https://www.jiqizhixin.com", "desc": "国内最权威的 AI 技术媒体"},
            {"name": "量子位", "url": "https://www.leiphone.com", "desc": "AI 行业动态和深度报道"},
            {"name": "HuggingFace 课程", "url": "https://huggingface.co/learn", "desc": "免费 NLP 和深度学习课程"},
            {"name": "吴恩达 AI 课程", "url": "https://www.deeplearning.ai", "desc": "AI 入门经典课程，全球数百万人学习"},
            {"name": "OpenAI Cookbook", "url": "https://cookbook.openai.com", "desc": "OpenAI API 实战教程和最佳实践"},
        ]
    },
    {
        "icon": "linecons-cloud",
        "id": "科学上网",
        "title": "科学上网",
        "items": [
            {"name": "西游-科学上网", "url": "https://xiyou4you.us/r/?s=13731627", "desc": "优秀的科学上网（略贵，但是贼稳，点击注册领取优惠券）"},
        ]
    },
]

def generate_card(item):
    return f'''
                    <div class="col-sm-3">
                        <div class="xe-widget xe-conversations box2 label-info" onclick="window.open('{item['url']}', '_blank')" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="{item['url']}">
                            <div class="xe-comment-entry">
                                <a class="xe-user-img">
                                    <img data-src="../assets/images/logos/default.png" class="lozad img-circle" width="40">
                                </a>
                                <div class="xe-comment">
                                    <a href="#" class="xe-user-name overflowClip_1">
                                        <strong>{item['name']}</strong>
                                    </a>
                                    <p class="overflowClip_2">{item['desc']}</p>
                                </div>
                            </div>
                        </div>
                    </div>'''

def generate_section(cat):
    items_html = ""
    for item in cat["items"]:
        items_html += generate_card(item)
    
    return f'''
        <h4 class="text-gray"><i class="linecons-tag" style="margin-right: 7px;" id="{cat['id']}"></i>{cat['title']}</h4>
        <div class="row">
{items_html}
        </div>'''

def generate_sidebar(cats):
    sidebar = ""
    for cat in cats:
        sidebar += f'''
                    <li>
                        <a href="#{cat['id']}" class="smooth">
                            <i class="{cat['icon']}"></i>
                            <span class="title">{cat['title']}</span>
                        </a>
                    </li>'''
    return sidebar

# Read original HTML
with open('/tmp/WebStackPage-rebuild/cn/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace title and meta
html = html.replace('WebStack.cc - 设计师网址导航', 'AI导航 - 2026 最新 AI 工具导航')
html = html.replace('<title>WebStack.cc - 设计师网址导航</title>', '<title>AI导航 - 2026 最新 AI 工具导航</title>')

# Find and replace sidebar menu
menu_start = html.index('<ul id="main-menu" class="main-menu">')
# Find the closing </ul> for main-menu (the one followed by </div></div><div class="main-content">)
search_pos = menu_start
while True:
    ul_close = html.index('</ul>', search_pos)
    after = html[ul_close:ul_close+100]
    if 'main-content' in after:
        menu_end = ul_close
        break
    search_pos = ul_close + 5

new_menu = generate_sidebar(NAV_CATEGORIES)
html = html[:menu_start + len('<ul id="main-menu" class="main-menu">')] + new_menu + html[menu_end:]

# Find and replace main content
content_start = html.index('<div class="main-content">')
# Find the closing </div> before footer
footer_pos = html.index('<footer', content_start)
content_end = html.rfind('</div>', content_start, footer_pos)

new_content_parts = []
for cat in NAV_CATEGORIES:
    new_content_parts.append(generate_section(cat))

new_content = '\n'.join(new_content_parts)
html = html[:content_start + len('<div class="main-content">')] + new_content + html[content_end:]

# Write new HTML
with open('/tmp/WebStackPage-rebuild/cn/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

total_items = sum(len(c['items']) for c in NAV_CATEGORIES)
print(f"✅ cn/index.html 已生成")
print(f"📊 共 {len(NAV_CATEGORIES)} 个分类，{total_items} 个网站")