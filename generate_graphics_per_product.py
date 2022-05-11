import os
import matplotlib.pyplot as plt

#Generate graphs per city, to look the behavior of destinated_are per year
def generate_graph(product,sub_df_per_product,missing_df,directory,scale,limit):
    #Make the graph
    fig = plt.figure(figsize = (30,20))

    #Percent of products that the graphs contain
    if type(missing_df) == type(sub_df_per_product):
        total = len(sub_df_per_product) + len(missing_df.loc[missing_df['product'] == product])
        percent = len(sub_df_per_product) / total
    else:
        percent = total = 0

    #Sets of graph
    plt.title(f'Destinated area to {product} per city / percent in this graph: {round(percent,2)} / total: {total}')
    plt.xlabel('years')
    plt.ylabel('destinated area')
    plt.grid()
    legends = []
    count = 0

    #Plot line without mising values
    for key,line in sub_df_per_product.fillna(-1).iterrows():
        year = []
        destinated_area = []
        count += 1
        legends.append(line.iloc[21] + ' ' + line.iloc[23])
        for position in range(0,21):
            if line.iloc[position] != -1:
                year.append(position)
                destinated_area.append(line.iloc[position])
        plt.plot(year,destinated_area,marker = 'o')

    #Plot the mean of the city
    legends.append('city mean')
    plt.plot(range(0,21),sub_df_per_product.iloc[:,0:21].mean(),'r--',marker = 'o')

    if limit != None:
        plt.ylim(limit)

    plt.yticks(scale)
    plt.legend(legends)

    if directory != None:
        plt.close()
    else:
        plt.show()

    #Save in a different directory
    if directory != None:
        local_save = os.path.join(os.path.abspath("."), f"graphics{os.sep}",(directory+os.sep),f"product_{product}.png")
        fig.savefig(local_save, dpi = fig.dpi)

    
