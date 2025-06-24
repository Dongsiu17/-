# %%
import os
import pandas as pd
import numpy as np
import random

from PIL import Image 

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import seaborn as sns
# %%
path=r'D:\edge download\archive\SMIDS'
classes=os.listdir(path)#列表，listdir（）列出该路径下所有文件名，listdirectory
print(classes)

# %%
def make_df(classes,base_path):
    data=[]
    for label in classes:# 两层路径，两层循环
        folder_path=os.path.join(base_path,label)  #用于将多个路径片段连接成一个路径字符串
        for file in os.listdir(folder_path):
            if file.endswith(('jpg','png','bmp')):# endswith(以什么结尾)
                file_path=os.path.join(folder_path,file)
                data.append((file_path,label))

    df=pd.DataFrame(data,columns=['file_path','label'])
    return df
df=make_df(classes,path)
print(df.shape)

# %%
df['label'].value_counts()
# %%
category_counts = df['label'].value_counts()


sns.set_style("whitegrid") 
colors = ['#66b3ff', '#ff9999', '#90EE90'] 
explode = (0.05, 0, 0)  
wedge_props = {'edgecolor': 'black', 'linewidth': 0.5}  
text_props = {'fontsize': 9, 'color': 'black'} 

plt.figure(figsize=(3.14, 3.14/1.618), dpi=600)
plt.pie(
    category_counts,
    labels=category_counts.index,
    autopct='%1.1f%%',
    pctdistance=0.5,
    startangle=90,
    colors=colors,
    explode=explode,
    shadow=True,
    wedgeprops=wedge_props,
    textprops=text_props
)

# 添加图例并调整标题
plt.title('label Category', fontsize=10, pad=12, fontweight='bold')
plt.legend(
    title='Categories',
    loc='best',
    bbox_to_anchor=(1, 0.5),
    frameon=False
)
plt.axis('equal')
plt.tight_layout() 

#plt.savefig('Stability Category.png',dpi=600)
plt.show()
# %%
df['label']
# %%
fig,axes=plt.subplots(3,3,figsize=(8,8))#fig代表整个图表的
#,axes是包含所有子图的数组,每个子图是以 Axes 对象存在于数组。
axes=axes.flatten()#flatten使...平整

# %%
for i,label in enumerate(classes):
    sample_images=random.sample(
    list(df['file_path'][df['label']==label]),3)
    sample_images
    break
    for j,img_path in enumerate(sample_images):
        img=mpimg.imread(img_path)
        axes[i * 3+ j].imshow(img)
        axes[i * 3+ j].axis('off')
        axes[i * 3+ j].set_title(label)
    
# %%
axes
# %%
print('hello')
# %%
