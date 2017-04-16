import numpy as np
import pandas as pd
from random import random
from bokeh.layouts import column,layout
from bokeh.models import ColumnDataSource,Select
from bokeh.plotting import figure,show
from bokeh.io import curdoc

dat_names = ['times','data1','data2','data3','data4','data5']
dat = pd.DataFrame(np.random.randn(10000,5))
dat = pd.concat([pd.DataFrame(np.array(range(1,10001))),dat],axis = 1)

dat.columns = dat_names
dat.columns[1:]

source1 = ColumnDataSource(data={'x': dat['times'], 'y': dat['data1']})
source2 = ColumnDataSource(data={'x': dat['times'], 'y': dat['data2']})
# Create plots and widgets


p1 = figure(width = 1000,height = 200)
p2 = figure(width = 1000,height = 200)
p1.line(x = 'x',y = 'y',source = source1)
p2.line(x = 'x',y = 'y',source = source2)

p2.x_range = p1.x_range

selectCh1 = Select(title = "Select CH",value = dat.columns[1],options = list(dat.columns[1:]))
selectCh2 = Select(title = "Select CH",value = dat.columns[1],options = list(dat.columns[1:]))

def callback1(attr, old, new):
    source1.data={'x': dat['times'], 'y': dat[selectCh1.value]}
selectCh1.on_change('value', callback1)

def callback2(attr, old, new):
    source2.data={'x': dat['times'], 'y': dat[selectCh2.value]}
selectCh2.on_change('value', callback2)


curdoc().add_root(column(selectCh1,p1,selectCh2,p2))