# deep-learning
```bash
conda env create -f environment.yml

conda env export > environment.yml

conda env export --name <environment_name> > environment.yml
```

你只要记住两点:
(1) 分类就用ResNet、分割就用U-Net、检测就用YOLO;
(2) 其余的精力你全部投入到数据上面去，把数据清理°好，想方法增加更多有用的数据，学习合理的运用多种trick才是王道。
发paper的可以忽略。