# %%
import matplotlib.pyplot as plt

img = plt.imread('/workspaces/data-science-foundations-python-scientific-stack-3084641LI/Ch02/challenge/flower.png')
img = img.copy()  # make img writable
plt.imshow(img)

#%%
type(img)
# %%
img.shape

# %%
# Draw a blue square around the flower
# Top-left: 190x350
# Bottom-right: 680x850
# Line width: 5