import numpy as np
import matplotlib.pyplot as plt

with open("res_10min_1chn.dat") as f:
    
    # Read data as ordered as: t active busy ratio

    lines = f.readlines()[3:]
    t = [line.split()[0] for line in lines]
    active = [line.split()[1] for line in lines]
    busy = [line.split()[2] for line in lines]
    ratio = [line.split()[3] for line in lines]

    f.close()


    # Plotting
    fig = plt.figure()

    ax1 = fig.add_subplot(211)
    ax1.set_title("ch1")    
    ax1.plot(t, active, c='r', label='active time')
    ax1.plot(t, busy, c='b', label='busy time')
    ax1.set_xlabel('Tick (s)')
    ax1.set_ylabel('Time (ms)')
    leg = ax1.legend()
    ax1.set_xlim([1,360])
    # ax1.set_ylim([0,1500])

    ax2 = fig.add_subplot(212)
    ax2.plot(t, ratio, 'k', label='ratio')
    ax2.set_xlabel('Tick (s)')
    ax2.set_ylabel('Ratio')
    ax2.set_xlim([1,360])
    leg = ax2.legend()

    plt.show()

    # fig.savefig('result.svg', format='svg', dpi=1200)
    fig.savefig('result.pdf', format='pdf')
    plt.close(fig)