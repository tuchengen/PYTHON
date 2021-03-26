from linerinster import  Tools

class PileCal(object):
    def __init__(self):
        self.f=open("E:\\foo.txt", "w+")
        pass

    def CalDiMianNeiLi(self,M,H,N,l0,n):
        M0=M/n+H/n*l0
        H0=H/n
        self.f.write(" 求地面处桩身内力：弯矩（FxL）")

def main():
    p=PileCal()
    p.CalDiMianNeiLi(1,1,1,1,1)
    p.f.write("dsdsdsd")
    p.f.close()

if __name__ == "__main__":
    main()  