class Solution:
    # @param numerator : integer
    # @param denominator : integer
    # @return a string
    def fractionToDecimal(self, numerator, denominator):

        if numerator == 0:
            return 0

        d = {'bef': [], 'aft': [], 'decimal': False, 'repeat': False, 'nneg': False, 'dneg': False, 'n': 0}
        nums = []


        if numerator < 0:
            numerator = -1 * numerator
            d['nneg'] = True

        if denominator < 0:
            denominator = -1 * denominator
            d['dneg'] = True

        while not d['repeat'] and numerator:
            if numerator > denominator:
                nums.append(numerator)
                d['bef'].append(str(numerator / denominator))
                numerator = numerator % denominator

            elif numerator < denominator:
                d['decimal'] = True
                nums.append(numerator)
                numerator = numerator * 10
                d['aft'].append(str(numerator / denominator))
                numerator = numerator % denominator

            else:
                if d['decimal'] == False:
                    nums.append(numerator)
                    d['bef'].append(str(numerator / denominator))
                    numerator = numerator % denominator
                else:
                    nums.append(numerator)
                    d['aft'].append(str(numerator / denominator))
                    numerator = numerator % denominator

            if numerator in nums:
                d['repeat'] = True
                d['n'] = numerator



        print nums
        print d['aft']

        if len(d['bef']) == 0:
            d['bef'].append(str(0))

        if d['repeat']:
            i = d['aft'].index(str(d['n']*10/denominator))
            x1 = ''.join(d['aft'][:i])
            x2 = ''.join(d['aft'][i:])

            a = '{}({})'.format(x1, x2)
        else:
            a = ''.join(d['aft'])

        b = ''.join(d['bef'])

        if d['decimal']:
            if d['nneg'] ^ d['dneg']:
                return '-{}.{}'.format(b, a)
            else:
                return '{}.{}'.format(b, a)

        else:
            if d['nneg'] ^ d['dneg']:
                return '-{}'.format(b)
            else:
                return b

# numerator = -1; denominator = 2
# numerator=1; denominator=3

# numerator=4; denominator=3
# numerator=-4; denominator=3

# numerator=-2147483648; denominator=-1

# numerator=8; denominator=7
# numerator=-1000; denominator=-1000

# numerator=87; denominator=22

print Solution().fractionToDecimal(numerator=numerator, denominator=denominator)