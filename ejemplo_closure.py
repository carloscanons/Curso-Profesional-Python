def make_division_by(n):
    def divisor(d):
        assert d!=0,"No puedes dividir entre cero"
        return d/n
    return divisor

division_by_10 = make_division_by(10)

def run():
    print(division_by_10(80))

if __name__=='__main__':
    run()