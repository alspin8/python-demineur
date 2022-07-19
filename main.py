from src.demineur import Demineur

def main():
    # demineur = Demineur(height=500, width=500)
    demineur = Demineur(rows=10, columns=10)
    demineur.run()
    
if __name__ == "__main__":
    main()