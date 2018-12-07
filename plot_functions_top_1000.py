def plotPublisher1000(fname='publishers_count.csv'):
    '''
    Author: Joshua Williams
    
    Makes a plot of the number of games that belong to each developer in
    the top 1000 ranking of our Dataset

    :fname (str): The name of the file that contains the dataframe [must be a .csv file]
    '''
    import pandas as pd
    import chartify as ch

    assert isinstance(fname, str) and '.csv' in fname, "Input is not str name of a .csv file!"
    # assert isinstance(fname2, str) and '.csv' in fname2, "Input is not str name of a .csv file!"

    data = pd.read_csv(fname)
    # data2 = pd.read_csd(fname2)

    data = pd.DataFrame({'publisher': list(data.columns.values[1:11]),
                         'count': list(data.values[0][1:11])})

    # Create a Chartify object for this plot
    chart = ch.Chart(blank_labels=True, y_axis_type='categorical')

    # Set Variables for plot
    chart.set_title('Top 10 Game Publishers with Well Received Games on Steam')
    chart.axes.set_xaxis_label('Number of Games Publisher has in Top 1000')
    chart.axes.set_yaxis_label('Publishers')
    chart.set_source_label('Steam Website')
    chart.plot.bar(data_frame=data,
                   categorical_columns='publisher',
                   numeric_column='count',
                   color_column='publisher',
                   categorical_order_ascending=True)

    chart.style.color_palette.reset_palette_order()

    chart.plot.text(data_frame=data,
                    categorical_columns='publisher',
                    numeric_column='count',
                    text_column='count',
                    color_column='publisher',
                    categorical_order_ascending=True)

    # Adjust the axis range to prevent clipping of the text labels.
    chart.axes.set_xaxis_range(0, 20)

    # Display Plot
    chart.show()


def plotGenre1000(fname='genres_count.csv'):
    '''
    Author: Joshua Williams
    
    Makes a plot of the number of games that belong to top 10 genres in
    our Dataset of top 1000 games

    :fname (str): The name of the file that contains the dataframe [must be a .csv file]
    '''
    import pandas as pd
    import chartify as ch

    assert isinstance(fname, str) and '.csv' in fname, "Input is not str name of a .csv file!"

    data = pd.read_csv(fname)
    genre_list = list(data.columns.values[1:11])

    genre_list[len(genre_list) - 1] = 'Multiplayer'
    data = pd.DataFrame({'genres': genre_list, 'count': list(data.values[0][1:11])})

    # Create a Chartify object for this plot
    chart = ch.Chart(blank_labels=True, x_axis_type='categorical')

    # Set Variables for plot
    chart.set_title('Top 10 Well Recieved Game Genres on Steam')
    chart.axes.set_xaxis_label('Genre')
    chart.axes.set_yaxis_label('Number of Games')
    chart.set_source_label('Steam Website')
    chart.plot.bar(data_frame=data,
                   categorical_columns='genres',
                   numeric_column='count',
                   color_column='genres',
                   categorical_order_ascending=False)

    chart.style.color_palette.reset_palette_order()

    chart.plot.text(data_frame=data,
                    categorical_columns='genres',
                    numeric_column='count',
                    text_column='count',
                    color_column='genres',
                    categorical_order_ascending=False)

    # Adjust the axis range to prevent clipping of the text labels.
    chart.axes.set_yaxis_range(0, 750)

    # Display Plot
    chart.show()


def plotSpecs1000(fname='specs_count.csv'):
    '''
    Author: Joshua Williams
    
    Makes a plot of the number of games that belong to top 10 specs in
    the top 1000 ranking of our Dataset

    :fname (str): The name of the file that contains the dataframe [must be a .csv file]
    '''
    import pandas as pd
    import chartify as ch

    assert isinstance(fname, str) and '.csv' in fname, "Input is not str name of a .csv file!"

    data = pd.read_csv(fname)
    data = pd.DataFrame({'specs': list(data.columns.values[1:11]), 'count': list(data.values[0][1:11])})

    # Create a Chartify object for this plot
    chart = ch.Chart(blank_labels=True, y_axis_type='categorical')

    # Set Variables for plot
    chart.set_title('Top 10 Specs Well Received Games Have')
    chart.axes.set_xaxis_label('Number of Games with Spec')
    chart.axes.set_yaxis_label('Specs')
    chart.set_source_label('Steam Website')
    chart.plot.bar(data_frame=data,
                   categorical_columns='specs',
                   numeric_column='count',
                   color_column='specs',
                   categorical_order_ascending=True)

    chart.style.color_palette.reset_palette_order()

    chart.plot.text(data_frame=data,
                    categorical_columns='specs',
                    numeric_column='count',
                    text_column='count',
                    color_column='specs',
                    categorical_order_ascending=True)

    # Adjust the axis range to prevent clipping of the text labels.
    chart.axes.set_xaxis_range(0, 1000)

    chart.show()


def plotPlatform1000(fname='platform_count.csv'):
    '''
    Author: Joshua Williams
    
    Makes a plot of the number of games that belong to each platform in
    the top 1000 ranking of our Dataset

    :fname (str): The name of the file that contains the dataframe [must be a .csv file]
    '''
    import pandas as pd
    import chartify as ch

    assert isinstance(fname, str) and '.csv' in fname, "Input is not str name of a .csv file!"

    data = pd.read_csv(fname)
    data = pd.DataFrame({'platform': list(data.columns.values[1:]), 'count': list(data.values[0][1:])})

    # Create a Chartify object for this plot
    chart = ch.Chart(blank_labels=True, x_axis_type='categorical')

    # Set Variables for plot
    chart.set_title('Number of Games Represented on Each Platform in Top 1000')
    chart.axes.set_xaxis_label('Platform')
    chart.axes.set_yaxis_label('Number of Games')
    chart.set_source_label('Steam Website')
    chart.plot.bar(data_frame=data,
                   categorical_columns='platform',
                   numeric_column='count',
                   color_column='platform')

    chart.style.color_palette.reset_palette_order()

    chart.plot.text(data_frame=data,
                    categorical_columns='platform',
                    numeric_column='count',
                    text_column='count',
                    color_column='platform')

    # Adjust the axis range to prevent clipping of the text labels.
    chart.axes.set_yaxis_range(0, 1100)

    chart.show()


def plotGenreToPlatform(fname1='df_genrecount_AGM PLAYISM.csv',
                        fname2='df_genrecount_Devolver Digital.csv',
                        fname3='df_genrecount_Daedalic Entertainment.csv',
                        fname4='df_genrecount_Electronic Arts.csv',
                        fname5='df_genrecount_Microsoft Studios.csv',
                        fname6='df_genrecount_Paradox Interactive.csv',
                        fname7='df_genrecount_SCS Software.csv',
                        fname8='df_genrecount_SEGA.csv',
                        fname9='df_genrecount_Sekai Project.csv',
                        fname10='df_genrecount_Ubisoft.csv'):
    '''
    Author: Joshua Williams
    
    Plots Genres goruped by developer

    :fname1 (str): The name of the file that a dataframe [must be a .csv file]
    :fname2 (str): The name of the file that a dataframe [must be a .csv file]
    :fname3 (str): The name of the file that a dataframe [must be a .csv file]
    :fname4 (str): The name of the file that a dataframe [must be a .csv file]
    '''
    import pandas as pd
    import chartify as ch

    assert isinstance(fname1, str) and '.csv' in fname1, "Input is not str name of a .csv file!"
    assert isinstance(fname2, str) and '.csv' in fname2, "Input is not str name of a .csv file!"
    assert isinstance(fname3, str) and '.csv' in fname3, "Input is not str name of a .csv file!"
    assert isinstance(fname4, str) and '.csv' in fname4, "Input is not str name of a .csv file!"
    assert isinstance(fname5, str) and '.csv' in fname5, "Input is not str name of a .csv file!"
    assert isinstance(fname6, str) and '.csv' in fname6, "Input is not str name of a .csv file!"
    assert isinstance(fname7, str) and '.csv' in fname7, "Input is not str name of a .csv file!"
    assert isinstance(fname8, str) and '.csv' in fname8, "Input is not str name of a .csv file!"
    assert isinstance(fname9, str) and '.csv' in fname9, "Input is not str name of a .csv file!"
    assert isinstance(fname10, str) and '.csv' in fname10, "Input is not str name of a .csv file!"

    data1 = pd.read_csv(fname1)
    data2 = pd.read_csv(fname2)
    data3 = pd.read_csv(fname3)
    data4 = pd.read_csv(fname4)
    data5 = pd.read_csv(fname5)
    data6 = pd.read_csv(fname6)
    data7 = pd.read_csv(fname7)
    data8 = pd.read_csv(fname8)
    data9 = pd.read_csv(fname9)
    data10 = pd.read_csv(fname10)

    publishers = ['AGM', 'DD', 'DE', 'EA', 'Micro', 'Para', 'SCS', 'SEGA', 'Sekai', 'Ubi']
    pub = []

    for i in publishers:
        for j in range(0, 3):
            pub.append(i)

    genres = data1['word'].tolist()[:3] + \
             data2['word'].tolist()[:3] + \
             data3['word'].tolist()[:3] + \
             data4['word'].tolist()[:3] + \
             data5['word'].tolist()[:3] + \
             data6['word'].tolist()[:3] + \
             data7['word'].tolist()[:3] + \
             data8['word'].tolist()[:3] + \
             data9['word'].tolist()[:3] + \
             data10['word'].tolist()[:3]

    counts = data1['count'].tolist()[:3] + \
             data2['count'].tolist()[:3] + \
             data3['count'].tolist()[:3] + \
             data4['count'].tolist()[:3] + \
             data5['count'].tolist()[:3] + \
             data6['count'].tolist()[:3] + \
             data7['count'].tolist()[:3] + \
             data8['count'].tolist()[:3] + \
             data9['count'].tolist()[:3] + \
             data10['count'].tolist()[:3]

    data = pd.DataFrame({'publishers': pub, 'word': genres, 'count': counts})

    # Create a Chartify object for this plot
    chart = ch.Chart(blank_labels=True, y_axis_type='categorical')

    # Set Variables for plot
    chart.set_title('Publishers to Genres')
    chart.axes.set_xaxis_label('Number of Games')
    chart.axes.set_yaxis_label('Publisher')
    chart.set_source_label('Steam Website')
    chart.plot.bar(data_frame=data,
                   categorical_columns=['publishers', 'word'],
                   numeric_column='count',
                   color_column='word')

    # Adjust the axis range to prevent clipping of the text labels.
    chart.axes.set_xaxis_range(0, 15)

    chart.show()