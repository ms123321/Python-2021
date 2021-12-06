# https://brainflow.readthedocs.io/en/stable/UserAPI.html#brainflow-board-shim
# need to change to the board to CYTON or GANGLION this is synthetic DATA
#change at board_id , might need board id number (int)
#https://openbci.com/community/publicly-available-eeg-datasets/

import pandas as pd
from matplotlib import style
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import matplotlib
import time
import sys
import brainflow
import numpy as np
from brainflow.board_shim import BoardShim, BrainFlowInputParams, LogLevels, BoardIds
from brainflow.data_filter import DataFilter, FilterTypes, AggOperations
from brainflow.ml_model import MLModel, BrainFlowMetrics, BrainFlowClassifiers, BrainFlowModelParams



def main(i):
    BoardShim.enable_dev_board_logger()
    BoardShim.disable_board_logger() #optional. take this out for initial setup for your board.
    BoardShim.set_log_file('log.txt') #non working
    
    # use synthetic board for demo
    params = BrainFlowInputParams()
    board_id = BoardIds.SYNTHETIC_BOARD.value
    board = BoardShim(board_id, params) # BOARD ARGUMENT IMPORTANT ! 
    
    eeg_channels = BoardShim.get_eeg_channels(board_id)
    sampling_rate = BoardShim.get_sampling_rate(board_id)
    timestamp = BoardShim.get_timestamp_channel(board_id)
    exg_channels = BoardShim.get_exg_channels(board_id)
    data3 = BoardShim.get_emg_channels(board_id)
    acceleration = BoardShim.get_accel_channels(board_id)
    #data3 = BoardShim.get_eeg_names(board_id)
    #data4 = BoardShim.get_gyro_channels(board_id)
   # eegnames = BoardShim.get_eeg_names(board_id)
   # data = board.get_board_data(board_id)
   # print(data)
    #print(eegnames)

    board.prepare_session()
    board.start_stream()
    
    style.use('fivethirtyeight')
    plt.title("Live EEG stream from Brainflow", fontsize=15)
    plt.ylabel("Data in millivolts", fontsize=15)
    plt.xlabel("\nTime", fontsize=10)
    keep_alive = True

    eeg1 = [] #lists to store eeg data
    eeg2 = []
    eeg3 = []
    eeg4 = []
    eeg5=  [] #new board
    eeg6=  [] #new board
    eeg7=  [] #new board
    eeg8=  []
    eeg9 = []
    eeg10 = []
    eeg11 = []
    eeg12 = []
    eeg13 = []
    eeg14 = []
    eeg15 = []
    eeg16 = []
    timex = [] #list to store timestamp

    while keep_alive == True:

     
        while board.get_board_data_count() < 250: #ensures that all data shape is the same
              time.sleep(0.0001)
        data = board.get_current_board_data(250)
        data2 = board.get_timestamp_channel(board_id) 
       
        

        # creating a dataframe of the eeg data to extract eeg values later
        eegdf = pd.DataFrame(np.transpose(data[eeg_channels]))
        eegdf_col_names = ["ch1", "ch2", "ch3", "ch4", "ch5", "ch6", "ch7",
                           "ch8", "ch9", "ch10", "ch11", "ch12", "ch13", "ch14", "ch15", "ch16"]
        eegdf.columns = eegdf_col_names
        
        af = pd.DataFrame(np.transpose(data[acceleration]))
        print("Acceleration Dataframe")
        print(af)
            
        eegdfstoredagain = pd.DataFrame(np.transpose(data[eeg_channels])) #stored the eeg array in new variable

        emg = pd.DataFrame(np.transpose(data[data3]))
        print("EMG dataframe")
        print(emg)
      
        
        #print(eegdfstoredagain)

        timedf = pd.DataFrame(np.transpose(data[timestamp])) ##  making another dataframe for the timestamps to access later(same as above)

        print("EEG Dataframe") #easy way to check what data is being streamed and if program is working
        print(eegdf)
        print("TIMESTAMPDATA")
        print(timedf)
         #isn't neccesary.
          # print(data)


######PRINT BOARD DATA 
        data2 = board.get_board_data()
        eegdf2 = pd.DataFrame(np.transpose(data2[eeg_channels]))
        eegdf2_col_names = ["ch1", "ch2", "ch3", "ch4", "ch5", "ch6", "ch7",
                           "ch8", "ch9", "ch10", "ch11", "ch12", "ch13", "ch14", "ch15", "ch16"]
        eegdf2.columns = eegdf_col_names
        print("BOARD DATA") # DATA 2 - BOARD DATA 
        print(eegdf2)

######PRINT average band power
   
        #data3 = board.get_avg_band_powers(board_id)    
       
        #eegdf3 = pd.DataFrame(np.transpose(data3[eeg_channels]))
        #eegdf3_col_names = ["ch1", "ch2", "ch3", "ch4", "ch5", "ch6", "ch7",
        #                   "ch8", "ch9", "ch10", "ch11", "ch12", "ch13", "ch14", "ch15", "ch16"]
        #eegdf3.columns = eegdf_col_names
        #print("average band power")
        #print(data3)

   



        for count, channel in enumerate(eeg_channels):
            # filters work in-place
            # Check Brainflow docs for more filters
            if count == 0:
                DataFilter.perform_bandstop(data[channel], sampling_rate, 60.0, 4.0, 4,
                                            FilterTypes.BUTTERWORTH.value, 0)  # bandstop 58 - 62
                DataFilter.perform_bandpass(data[channel], sampling_rate, 21.0, 20.0, 4,
                                            FilterTypes.BESSEL.value, 0)  # bandpass 11 - 31
            if count == 1:
                DataFilter.perform_bandstop(data[channel], sampling_rate, 60.0, 4.0, 4,
                                            FilterTypes.BUTTERWORTH.value, 0)  # bandstop 58 - 62
                DataFilter.perform_bandpass(data[channel], sampling_rate, 21.0, 20.0, 4,
                                            FilterTypes.BESSEL.value, 0)  # bandpass 11 - 31
            if count == 2:
                DataFilter.perform_bandstop(data[channel], sampling_rate, 60.0, 4.0, 4,
                                            FilterTypes.BUTTERWORTH.value, 0)  # bandstop 58 - 62
                DataFilter.perform_bandpass(data[channel], sampling_rate, 21.0, 20.0, 4,
                                            FilterTypes.BESSEL.value, 0)  # bandpass 11 - 31
            if count == 3:
                DataFilter.perform_bandstop(data[channel], sampling_rate, 60.0, 4.0, 4,
                                            FilterTypes.BUTTERWORTH.value, 0)  # bandstop 58 - 62
                DataFilter.perform_bandpass(data[channel], sampling_rate, 21.0, 20.0, 4,
                                            FilterTypes.BUTTERWORTH.value, 0)

#########################################data 2 filters or backup filter module - CHANGE data2 source input and output 
        for count, channel in enumerate(data3): # BOARD DATA FILTERS , or backup filters, change data2 to same source as data, change filters
            # filters work in-place
            # Check Brainflow docs for more filters
            if count == 0:
                DataFilter.perform_bandstop(data2[channel], sampling_rate, 60.0, 4.0, 4,
                                            FilterTypes.BUTTERWORTH.value, 0)  # bandstop 58 - 62
                DataFilter.perform_bandpass(data[channel], sampling_rate, 21.0, 20.0, 4,
                                            FilterTypes.BESSEL.value, 0)  # bandpass 11 - 31
            if count == 1:
                DataFilter.perform_bandstop(data2[channel], sampling_rate, 60.0, 4.0, 4,
                                            FilterTypes.BUTTERWORTH.value, 0)  # bandstop 58 - 62
                DataFilter.perform_bandpass(data[channel], sampling_rate, 21.0, 20.0, 4,
                                            FilterTypes.BESSEL.value, 0)  # bandpass 11 - 31
            if count == 2:
                DataFilter.perform_bandstop(data2[channel], sampling_rate, 60.0, 4.0, 4,
                                            FilterTypes.BUTTERWORTH.value, 0)  # bandstop 58 - 62
                DataFilter.perform_bandpass(data[channel], sampling_rate, 21.0, 20.0, 4,
                                            FilterTypes.BESSEL.value, 0)  # bandpass 11 - 31
            if count == 3:
                DataFilter.perform_bandstop(data2[channel], sampling_rate, 60.0, 4.0, 4,
                                            FilterTypes.BUTTERWORTH.value, 0)  # bandstop 58 - 62
                DataFilter.perform_bandpass(data[channel], sampling_rate, 21.0, 20.0, 4,
                                            FilterTypes.BUTTERWORTH.value, 0)
##########################################


        eeg1.extend(eegdf.iloc[:, 0].values) # I am using OpenBCI Ganglion board, so I only have four channels.
        eeg2.extend(eegdf.iloc[:, 1].values) # If you have a different board, you should be able to copy paste
        eeg3.extend(eegdf.iloc[:, 2].values) # these commands for more channels.
        eeg4.extend(eegdf.iloc[:, 3].values)
        eeg5.extend(eegdf.iloc[:, 4].values) #new board
        eeg6.extend(eegdf.iloc[:, 5].values) #new board
        eeg7.extend(eegdf.iloc[:, 6].values) #new board
        eeg8.extend(eegdf.iloc[:, 7].values)
        eeg9.extend(eegdf.iloc[:, 8].values)
        eeg10.extend(eegdf.iloc[:, 9].values)
        eeg11.extend(eegdf.iloc[:, 10].values)
        eeg12.extend(eegdf.iloc[:, 11].values)
        eeg13.extend(eegdf.iloc[:, 12].values)
        eeg14.extend(eegdf.iloc[:, 13].values)
        eeg15.extend(eegdf.iloc[:, 14].values)
        eeg16.extend(eegdf.iloc[:, 15].values)
        # new board
        timex.extend(timedf.iloc[:, 0].values)  #
        

###########chanel 1
        

        #plotting eeg data

        plt.cla()

        plt.figure(1)
        plt.plot(timex, eeg1, label="Channel 1", color="red")
        plt.ylabel("Data in millivolts", fontsize=15)
        plt.xlabel("\nTime", fontsize=10)
        
        plt.figure(2)
        plt.plot(timex, eeg2, label="Channel 2", color="blue")

        plt.figure(3)
        plt.plot(timex, eeg3, label="Channel 3", color="orange")

        plt.figure(4)
        plt.plot(timex, eeg4, label="Channel 4", color="purple")

        plt.figure(5)
        plt.plot(timex, eeg5, label="Channel 5", color="blue")

        plt.figure(6)
        plt.plot(timex, eeg6, label="Channel 6", color="yellow")

        plt.figure(7)
        plt.plot(timex, eeg7, label="Channel 7", color="blue")

        plt.figure(8)
        plt.plot(timex, eeg8, label="Channel 8", color="black")
        
        plt.figure(9)
        plt.plot(timex, eeg9, label="Channel 9", color="cyan")
        
        plt.figure(10)
        plt.plot(timex, eeg10, label="Channel 10", color="magenta")
        
        plt.figure(11)
        plt.plot(timex, eeg11, label="Channel 11", color="teal")
              
        plt.figure(12)
        plt.plot(timex, eeg12, label="Channel 12", color="gold")
        

        plt.figure(13)
        plt.plot(timex, eeg13, label="Channel 13", color="black")
        
        plt.figure(14)
        plt.plot(timex, eeg14, label="Channel 13", color="green")
               
        plt.figure(15)
        plt.plot(timex, eeg15, label="Channel 13", color="orange")
        
        plt.figure(16)
        plt.plot(timex, eeg16, label="Channel 13", color="red")
        














        plt.show()
        keep_alive = False #resetting stream so that matplotlib can plot data
############chanel 2 
        
        
        #keep_alive = True





    #print('Data From the File')
   # print(restored_df.head(10))
   # print(restored_df2)


########PRINT DATA ############################################################################################

        DataFilter.write_file(data, 'Board Data.csv', 'w')  # use 'a' for append mode
        restored_data = DataFilter.read_file('test.csv')
        restored_df = pd.DataFrame(np.transpose(restored_data))
        print('BOARD DATA ON FILE')
        print(restored_df.head(10))
## PRINTS THE BOARD DATA
 

        DataFilter.write_file(data2, 'TIMESTAMP CHANNELS.csv', 'w')  # use 'a' for append mode
        restored_data2 = DataFilter.read_file('test2.csv')
        restored_dft = pd.DataFrame(np.transpose(restored_data2))
        print('GET TIMESTAMP CHANNELS on FILE')
        print(restored_dft.head(10))   
## PRINTS TIMESTAMP DATA
        


        #DataFilter.write_file(emg, 'EMG CHANNELS.csv', 'w')  # use 'a' for append mode
        #restored_dataemf = DataFilter.read_file('test2.csv')
        #restored_dft = pd.DataFrame(np.transpose(restored_dataemf))
       # print("EMG CHANNELS - FILE TRANSSFER NOT WORKING") 
        #print(emg)
## PRINTS EMG DATA



        
        #DataFilter.write_file(data3, 'emg data.csv', 'a')  # use 'a' for append mode
        #restored_data3 = DataFilter.read_file('test3.csv')
        #restored_dfm = pd.DataFrame(np.transpose(restored_data3))
        #print('emgdata')
        #print(restored_dfm.head(10))
## prints gyro data


    
    



    board.stop_stream()
    board.release_session()









ani = FuncAnimation(plt.gcf(), main, interval=1000) #this essentially calls the function several times until keyboard interrupt
#plt.tight_layout()
#plt.autoscale(enable=True, axis="y", tight=True)
plt.show()



########
                
