from util import *

send_gdb('break breakpoint')
expect_gdb('Breakpoint 1')
send_gdb('c')
expect_gdb('Breakpoint 1')

ok()
