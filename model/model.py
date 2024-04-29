import copy


class Model:
    def __init__(self):
        self.n_iterazioni = 0
        self.n_soluzioni = 0
        self.soluzioni = []


    def risolvi_quadrato(self, N):
        self.n_iterazioni = 0
        self.n_soluzioni = 0
        self.ricorsione([], set(range(1, N*N+1)), N)


    def ricorsione(self, parziale,  rimanenti, N):
        self.n_iterazioni += 1
        if len(parziale) == N*N:
            #if parziale==[8,3,4,1,5,9,6,7,2]:
                if self.is_soluzione(parziale, N):
                    print(parziale)
                    self.n_soluzioni += 1
                    self.soluzioni.append(copy.deepcopy(parziale))

        else:
            for i in rimanenti:
                parziale.append(i)
                nuovi_rimanenti = copy.deepcopy(rimanenti)
                nuovi_rimanenti.remove(i)
                self.ricorsione(parziale, nuovi_rimanenti,N)
                parziale.pop()
    def stampa_soluzione(self, soluzione, N):
        print('--------')
        for row in range(N):
            print([v for v in soluzione[row*N: (row+1)*N ]])
        print('--------')

    def is_soluzione(self, parziale, N):
        numero_magico = N*(N*N+1)/2

        for row in range(N):
            somma = 0
            sottolista = parziale[row*N: (row+1)*N]
            for elemento in sottolista:
                somma += elemento
            if somma != numero_magico:
                return False

        for col in range(N):
            somma = 0
            sottolista = parziale[0*N + col: (N-1)*N+col+1:N]
            for elemento in sottolista:
                somma += elemento
            if somma != numero_magico:
                return False
        #diagonale 1
        somma = 0
        for riga_col in range(N):
            somma += parziale[riga_col*N+riga_col]

        if somma!=numero_magico:
            return False


        #diagonale 2
        somma = 0
        for riga_col in range(N):
            somma += parziale[riga_col * N + (N - 1 -riga_col)]

        if somma != numero_magico:
            return False

        return True

    def is_soluzione_parziale(self, parziale, N):
        numero_magico = N*(N*N+1)/2
        somma = 0
        n_righe = len(parziale)//N
        for row in range(n_righe):
            sottolista = parziale[row*N: (row+1)*N]
            for elemento in sottolista:
                somma += elemento
            if somma != numero_magico:
                return False
        somma = 0
        #n_col =
        for col in range(N):
            sottolista = parziale[0*N + col: (N-1)*N+col+1:N]
            for elemento in sottolista:
                somma += elemento
            if somma != numero_magico:
                return False
        #diagonale 1
        somma = 0
        for riga_col in range(N):
            somma += parziale[riga_col*N+riga_col]

        if somma!=numero_magico:
            return False


        #diagonale 2
        somma = 0
        for riga_col in range(N):
            somma += parziale[riga_col * N + (N - 1 -riga_col)]

        if somma != numero_magico:
            return False

        return True

if __name__=="__main__":
    N = 3
    model = Model()
    model.risolvi_quadrato(N)
    print(f"Quadrato di lato {N} risolto con {model.n_iterazioni} iterazioni")
    print(f"Trovate {model.n_soluzioni} soluzioni")
    for i in range(len(model.soluzioni)):
        model.stampa_soluzione(model.soluzioni[i], N)