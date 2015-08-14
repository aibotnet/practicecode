
def get_text(name):
   print name
   return "lorem ipsum, {0} dolor sit amet".format(name)

def p_decorate(func):
   print "1",func
   def func_wrapper(name):
       print name,'--'
       return "<p>{0}</p>".format(func(name))
   print 'vikas'
   return func_wrapper

my_get_text = p_decorate(get_text)

print my_get_text("John")

print '--------------------------------'


p_decorate(get_text('john'))


'''
1 <function get_text at 0x7eff59518578>
vikas
John --
John
<p>lorem ipsum, John dolor sit amet</p>
--------------------------------
john
1 lorem ipsum, john dolor sit amet
vikas
'''

