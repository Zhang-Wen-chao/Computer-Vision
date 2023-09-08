# deep-learning
我也忘记为什么要开这个仓库了。

需要学什么东西？？

第一步，把所有积攒的内容整理一下。然后制定一些非常标题党的小目标。比如

一小时学完numpy

pandas 建立在numpy之上。
matplotlib

一小时学完pytorch

一天学会Python

一天写完AI发展历史，（手写代码）

一天搞定嵌入式

一天搞定树莓派，对现在安装的还是树莓派的系统，找树莓派社区，赶紧过一遍。

一天学会cpp

一天搞定slam算法

一天写完slam论文

一天读50篇论文



开始复现stable diffusion和dalle 2

   - [ ] vit，clip。对齐，位置，第一步。generation，dalle2：给定smiles，就可以当作图像的特征，但未必是真的图像特征。再decoder，autoregressve、diffusion。第二种做法就是stable diffussion。先做一个图像的特征，aotuencoder，给定condition生成一个图像的特征。反正第一步是对齐文本和图像的特征。给个graph生成图像，给个文本生成图像，可以都做。

```bash
conda env create -f environment.yml

conda env export > environment.yml

conda env export --name <environment_name> > environment.yml

```