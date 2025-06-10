import numpy as np
def percent_correct(Y, T):
    return np.mean(T == Y) * 100
#-----------------------------------------------------------------
import pandas
def confusion_matrix(Y_classes, T):
    class_names = np.unique(T)
    table = []
    for true_class in class_names:
        row = []
        for Y_class in class_names:
            row.append(100 * np.mean(Y_classes[T == true_class] == Y_class))
        table.append(row)
    conf_matrix = pandas.DataFrame(table, index=class_names, columns=class_names)
    print('Confusion Matrix:')
    return conf_matrix.style.background_gradient(cmap='Blues').format("{:.1f}")
#-----------------------------------------------------------------
import neuralnetworksA4 as nn
def experiment(data, hyperparameters):
    l_structures, l_methods, l_epochs, l_lrates = hyperparameters
    Xtrain, Ttrain, Xval, Tval, Xtest, Ttest = data
    n_inputs = Xtrain.shape[1]
    n_outpus = len(np.unique(Ttrain))
    summary = pandas.DataFrame(columns=['Structure','Method','Epochs','Learning Rate','Training Acc','Validation Acc','Test Acc'])
    summary_plot = []
    for e_structure in l_structures:
        for e_method in l_methods:
            for e_epoch in l_epochs:
                for e_lrate in l_lrates:
                    nnet = nn.NeuralNetworkClassifier(n_inputs, e_structure, n_outpus)
                    nnet.train(Xtrain, Ttrain, n_epochs=e_epoch, method=e_method, learning_rate=e_lrate)
                    metrics = [percent_correct(nnet.use(X)[0], T) for X, T in zip([Xtrain, Xval, Xtest], [Ttrain, Tval, Ttest])]
                    print('Training Acc:{:.2f}% Validation Acc:{:.2f}% Test Acc:{:.2f}%'.format(metrics[0], metrics[1], metrics[2]))
                    e_lrate = '-' if (e_method == 'scg') else e_lrate
                    summary.loc[len(summary.index)] = [e_structure, e_method, e_epoch, e_lrate, metrics[0], metrics[1], metrics[2]]
                    summary_plot.append([nnet.get_performance_trace(), nnet.use(Xtest)[0], Ttest])
                    if(e_method == 'scg'):
                        break #ignore learning rates for scg
    return summary, summary_plot
#-----------------------------------------------------------------
def show_topN(summary, top=10):
    return summary.sort_values('Validation Acc', ascending=False).head(top)
#-----------------------------------------------------------------
import matplotlib.pyplot as plt
def show_best(data, title, index_best=-1):
    summary = data['summary']
    plots = data['plots']
    if (index_best < 0):
        index_best = summary.sort_values('Validation Acc', ascending=False).head(1).index[0]
        print('The best hyper-parameter configuration found was #', index_best)
    else:
        print('Showing results for configuration #', index_best)
    display(confusion_matrix(plots[index_best][1], plots[index_best][2]))
    plt.rcParams["figure.figsize"] = (6,3)
    plt.plot(plots[index_best][0],'-',label=title)
    plt.xlabel('Epochs')
    plt.ylabel('Data likelihood')
    plt.legend()
    plt.show()
#-----------------------------------------------------------------