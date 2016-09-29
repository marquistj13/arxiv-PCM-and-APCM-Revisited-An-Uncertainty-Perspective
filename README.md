## 算法原理大揭秘
一个pcm聚类算法已经可以了，为何还要有后续的改进呢？  
因为世界没有那么simple，如果所有data组成的cluster都是 well-separated,那么很好，我们就不需要那么多trick了。  
问题就出在noise上，有了noise，well-separated的cluster就会挨得很近，变得难以区分，也就有了我们研究人员的饭碗。所以，感谢noise！  
但恕我寡闻，我为啥很少遇到从noise角度对这个聚类问题进行分析的呢？难道是因为怕揭示了“本质”以后，大家都没了饭碗？  
当然，我倾向于认为，从noise角度去解决它仅仅是一个角度，因为造成clustering困难的肯定不止是noise一个。但我认为从noise角度是可以干掉
很大一部分的问题的。

此算法在统一pcm和apcm的同时，从noise角度来重新阐述两个算法。  
我们cluster之间本来好好的，因为noise的存在，看起来靠的越来越近，怎么办？  
你的点跑到我的地盘上了，来干扰我，造成了我对自己评估的不确定性（也就是自身带宽估计的不确定性），使我不得开心颜。  
此算法采用“敌进我退”的战术，你不是用noise point来干扰我么，我知道自己估计出来的带宽是不准的了，即不确定性比较大了，为了
准确估计聚类中心（忘了说了，这个聚类中心的估计是我最重要的使命，相当于扛军旗了吧？ 一个点对于一个cluster的隶属度，取决于聚类中心和
该cluster的带宽），我可以适当增加带宽估计的不确定度。但不能增的太多，要不然又要受到敌方noise点的干扰啦。

## 各个文件说明
### 首先是对apcm各种策略的分类
* apcm.py 对应fig1.py  
即原pcm+bandwidth改为不断调整的mean absolute deviation+加入
 $\alpha$ 动态调整目标函数（其实也是一种先验信息的嵌入形式） 
* apcm_without_alpha.py 对应apcm_without_alpha.py  
即原pcm+bandwidth改为不断调整的mean absolute deviation
* opcm.py 对应fig1_opcm.py  
opcm其实就是original pcm的缩写，即原pcm+bandwidth改为不断调整的variance
注意：本文件中的adapt_ita(self)函数我做了改动，分别对应原pcm和改动后的。
用的时候注意切换注释（从该函数很容易找到改动的地方），要改成原pcm的话貌似还要在
 fit(self)函数中注释掉self.adapt_ita()的调用，即不更新每个cluster的带宽。
 好了还是将pcm独立成一个新文件吧，就叫pcm.py
* pcm.py  
各个cluster的bandwidth一经初始化就不再更新，因此性能强烈依赖于初始化

### 下面就是主要文件了
* pcm_fs2.py 对应fig1_pcm_fs2.py  
就是在apcm的基础上对隶属度函数进行Type2的修正。
* exlore_object_func.py  
探索隶属度的惩罚曲线及其导数曲线