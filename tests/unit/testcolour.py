
# coding: utf-8

# In[50]:

import unittest
import colourlovers as cl
from mock import Mock
import random
import hamcrest


# In[ ]:




# In[51]:

class TestColourLoversApi(unittest.TestCase):
    
    def setUp(self):
        #self.colornam = ('#6b4106')
        self.rabdcik = list(['#6b4106', '#FFFFFF', '#540918'])
        self.ranchoi = random.choice(self.rabdcik)
        
        
        #Setup a list of random colours (5), 
        

    def test_can_retrieve_color_from_hex_value(self):
         #cl_api = cl.ColourLovers()
            
        #res = cl_api.color(hexstr)
            #self.assertEquals(len(res), 1)
            #self.assertEquals(type(colornam, cl.Colour)
        self.assertEquals('#6b4106', '#6b4106')
            
    
    def test_random_colours_to_dict(self):
        #This tests retrieving random colours from
        #colourlovers and saving a json file with details.
        #This is for hostname assign.
        clx = cl.ColourLovers()
        
        res = clx.color(self.ranchoi)
        mydict = dict()

        mydict.update({'hex' : res})
        
        hamcrest.assert_that (mydict) == hamcrest.not_none

        
    #def test_retrieving_color_from_invalid_hex_raises_an_exception(self):
    #    cl_api = cl.ColourLovers()

     #   self.assertRaises(cl.ColourLoversError, cl_api.color, '6B410')

        
    def tearDown(self):
        #self.colornam.dispose()
        self.colornam = None
            
    
            
#if __name__ == '__main__':
#    unittest.main()


# In[38]:

#colornam = list(['6B4106', '#6b4106'])


# In[39]:

#colornam


# In[7]:

''''

class testcolour(unittest.TestCase):
    def set_up(self):
        self.li
        liscolorid.append(id=14, 'title)
    def test_rgbtocolor(self):
        #self.
        colourlovers.Colour
        
        colourlovers.RGB.hex(0000000)
'''   


# In[8]:

#colourlovers.Colour()

#cl = ColourLovers()


# In[9]:

#import colourlovers


# In[10]:

#cwhit = ColourLovers.Colour('#000000')


# In[42]:

#'ffffff'.hex


# In[ ]:



