class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        A = A.split('/')
        A = [a for a in A if a]

        # print A

        stack = []
        for x in A:
            if not x == '..' and not x == '.':
                stack.append(x)
            elif x == '.':
                pass
            else:
                if len(stack):
                    stack.pop()


        # print stack

        stack = '/'.join(stack)
        return '/{}'.format(stack)





# A = "/a/./b/../../c/"
# A = '/home'
# A = '/home_dir/z001ldl/../z002axs/'
# A = '/../'
# A = '/..'
# A = "/./../../giq/xns/zvk/../vkd/qhp/pyf/wie/atv/thv/./kqs/seq/fzw/cav/./../.././rjn/elx/gyn/lla/gkd/zig/qud/vyx/./eqd/ple/vst/loc/./../uak/wvz/vxe/ibc/../bns/psb/./kjo/bky/oks/./cjg/yyh/spf/abt"
# A = "/home//fold"
# print A
print Solution().simplifyPath(A)