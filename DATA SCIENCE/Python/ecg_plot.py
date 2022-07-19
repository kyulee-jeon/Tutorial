# df_x.shape == (5000,12)

def show_waveform(df_x):
    for i in a:
        lead = df_x[str(i)].to_numpy()
        plt.plot(lead)
        plt.title(str(i))
        plt.show()
