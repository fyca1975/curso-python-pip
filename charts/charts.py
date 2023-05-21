import matplotlib.pyplot as plt

def generar_pie():
    labels = ['A','B','C']
    values = [12,5,3]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()

