## 各个文件说明
### 首先是对apcm各种策略的分类
* apcm.py 对应fig1.py
即原pcm+bandwidth改为不断调整的mean absolute deviation+加入
 $\alpha$ 动态调整目标函数（其实也是一种先验信息的嵌入形式） 
* apcm_without_alpha.py 对应apcm_without_alpha.py
即原pcm+bandwidth改为不断调整的mean absolute deviation
* opcm.py 对应fig1_opcm.py
opcm其实就是original pcm的缩写，即原pcm+bandwidth改为不断调整的variance