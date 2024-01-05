系统核心能力分块
1、拆句子
2、生成srt
3、生成语音mp3
4、srt+mp3 音文对齐
5、chatgpt 小说背景prompt 加翻译
    回去后，先用chatgpt api 翻译为一句一句的英语，然后，分段，然后直接手动开画，画玩的全部保存一波
    保存完毕后，生成视频
    然后分析下，中间每一步，那一步用时最多，在明确步骤的情况下（写代码的时间不算进去）
    1、如何让生成的prompt可以一直生效
        openai 中文仓库 https://openai.xiniushu.com/docs/libraries
    2、准备一份玄幻小说中文和英语对照表
        https://immortalmountain.wordpress.com/glossary/wuxia-xianxia-xuanhuan-terms/
        https://owlcation.com/humanities/A-Wuxia-Glossary
        https://owlcation.com/humanities/A-Beginners-Guide-to-Wuxia

    看下这些prompt 是否可以满足需求,下面这些东西似乎被叫做 GPTs 
    参考这个文章  https://new.qq.com/rain/a/20231206A003TT00
    还有这个 https://hub.baai.ac.cn/view/33276
    这是如何创建GPTs https://zhuanlan.zhihu.com/p/666176123
        https://36kr.com/p/2512454329258243
        https://chat.openai.com/g/g-iWNYzo5Td-midjourney-generator
        https://chat.openai.com/g/g-iQQ6Qfd6j-wallpaper-gpt
        https://chat.openai.com/g/g-D21BibKO9-art-engineer
        https://chat.openai.com/g/g-B3qi2zKGB-comfyui-assistant
    测试一下通意千问的数学解答能力
    这里还有一些写代码的ai
    https://chat.openai.com/g/g-AVrfRPzod-react-ai
    了解这个插件
    https://github.com/s0md3v/sd-webui-roop


仙侠背景翻译文章
    https://www.goldenelixir.com/files/Wang_Mu_Foundations_of_Internal_Alchemy_SAMPLE.pdf
    
6、英语文章抽关键词
7、生成图和视频
8、合成模块

【！！！】直播回放 OPENAI 开发者大会看一遍

简单设计
1、核心能力之间互相独立
2、数据通过文件交流（结果都会保存一次）
    互相交流的文件格式急需定义，比如什么文件是数据，怎么读？
3、核心流程走通后，外部接UI

目标
1、对于中短文案可以迅速生成声音可以，画面相关的短视频