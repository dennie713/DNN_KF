import cupy as cp
<<<<<<< HEAD
# import numpy as cp
=======
<<<<<<< HEAD
# import numpy as cp
=======
>>>>>>> 306d347394907d950140afa14d4e6ba645070c37
>>>>>>> 6a91b5d423c756b82df34fa1d19ee44af9e1ac77
import numpy as np
import torch
import torch.nn as nn
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import matplotlib.pyplot as plt
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import LSTM, dataset_arrange
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 6a91b5d423c756b82df34fa1d19ee44af9e1ac77
import setLSTMConfig
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# 馬達實際資料
<<<<<<< HEAD
path1 = 'motor_dataset/Motor_x_data_ips650_g50.txt'
path2 = 'motor_dataset/Motor_x_data_ips650_g50.txt'
=======
path1 = 'motor_dataset/Motor_x_data_combine_diff.txt'
path2 = 'motor_dataset/Motor_x_data_combine_diff.txt'
>>>>>>> 6a91b5d423c756b82df34fa1d19ee44af9e1ac77
x_data, x_true, x_k_update_data, x_cmd, km_y_data, x_tel, x_input_data_all, P_data, P_k_update_data, KCP_data, P_input_data_all = dataset_arrange.loadMotorData(path1, path2)

# 參數設置
setConfig = setLSTMConfig.LSTMConfig()
x_input_size, x_output_size, hidden_size, num_layers, dropout, P_input_size, P_output_size = setConfig.getLSTMConfig()

# 加載模型
x_lstm_model_loaded = LSTM.LSTM_KF(x_input_size, hidden_size, x_output_size, num_layers, dropout)  # 創建模型實例
x_lstm_model_loaded.load_state_dict(torch.load('motor/motor_model/x_model.pth', weights_only=True))  # 加載權重
x_lstm_model_loaded.eval()  # 將模型設置為評估模式
x_lstm_model_loaded = x_lstm_model_loaded.to(device)
# hidden_size = 128
start_size = 0
validation_size = len(x_k_update_data) # diff: 14683 # same: 23000
data_set_size = start_size + validation_size

<<<<<<< HEAD
=======
=======
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# 參數設置
hidden_size = 128
start_size = 0
validation_size = 10000
data_set_size = start_size + validation_size

# 準備輸入數據
# 讀取檔案
# path1 = ['E:/cmake_mouse_boundary_v9_1/build/IPS750_G50_F_motion.txt'] #馬達資料.txt路徑
# path2 = ['E:/cmake_mouse_boundary_v9_1/build/IPS750_G50_F_mouse.txt']  #滑鼠資料.txt路徑
# x_kf_update_data, P_kf_update_data, K_update_data, k_y_update_data, KCP_data, H, Pos, PosCmd, VelCmd, AccCmd, PosCmd_AddNoise, VelCmd_AddNoise, AccCmd_AddNoise = KF.KF_Process(path1, path2)
# x_k_update_data, x_k_predict_data, P_k_update_data, P_k_predict_data, k_y_data, KCP_data, z_data, x_true_data, x_true_data_noise, P_k_data, prediction_errors_data = KF_training_data.KF_Process(data_set_size)
# z = PosCmd
# x_true = cp.array([PosCmd, 
#                    VelCmd,
#                    AccCmd])

# 模擬\資料
# x_data, x_k_update_data, k_y_data, x_tel, x_true, x_true_noise, x_obsve, x_input_data_all, x_k_predict_data, P_data, P_k_update_data, KCP_data, P_input_data_all = load_test.load_data('x_data_all.txt', 'P_data_all.txt')
# x_input_data_all = np.loadtxt('x_input_data_all_normalized.txt', delimiter=' ')
# P_input_data_all = np.loadtxt('P_input_data_all_normalized.txt', delimiter=' ')

# 馬達實際資料
path1 = 'motor_dataset/Motor_x_data_ips300_cycle200.txt'
path2 = 'motor_dataset/Motor_P_data_ips300_cycle200.txt'
x_data, x_true, x_k_update_data, x_cmd, km_y_data, x_tel, x_input_data_all, P_data, P_k_update_data, KCP_data, P_input_data_all = dataset_arrange.loadMotorData(path1, path2)
# x_data = np.loadtxt('./motor_dataset/Motor_x_data.txt')
# P_data = np.loadtxt('./motor_dataset/Motor_P_data.txt')
# # Pos, pose, vele, acce, km_y_data, x_tel_data
# x_input_data_all = x_data[:, 1:]
# x_true = x_data[:,0]
# x_k_update_data = x_data[:, 1:4]
# # Pm_data, kcp_data
# P_input_data_all = P_data
# P_k_update_data = P_data[:, :9]
# KCP_data = P_data[:, 9:17]

>>>>>>> 306d347394907d950140afa14d4e6ba645070c37
>>>>>>> 6a91b5d423c756b82df34fa1d19ee44af9e1ac77
P_true = cp.array([[1e-7, 1e-7, 1e-7],
                   [1e-7, 1e-7, 1e-7],
                   [1e-7, 1e-7, 1e-7]])

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 6a91b5d423c756b82df34fa1d19ee44af9e1ac77
# # 加載模型
# P_lstm_model_loaded = LSTM.LSTM_KF(input_size, hidden_size, output_size)  # 創建模型實例
# P_lstm_model_loaded.load_state_dict(torch.load('motor/motor_model/P_model.pth', weights_only=True))  # 加載權重
# P_lstm_model_loaded.eval()  # 將模型設置為評估模式
# P_lstm_model_loaded = P_lstm_model_loaded.to(device)

# --------x_model loading --------#
x_lstm_output_data = []
<<<<<<< HEAD
=======
=======
# --------x_model loading --------#
# 設置模型參數
input_size = 7  # 根據需要的特徵數
output_size = 3    # 假設輸出有兩個維度

# 加載模型
x_lstm_model_loaded = LSTM.LSTM_KF(input_size, hidden_size, output_size)  # 創建模型實例
x_lstm_model_loaded.load_state_dict(torch.load('motor/motor_model/x_lstm_kf_model.pth', weights_only=True))  # 加載權重
x_lstm_model_loaded.eval()  # 將模型設置為評估模式
x_lstm_model_loaded = x_lstm_model_loaded.to(device)

x_lstm_output_data = []

>>>>>>> 306d347394907d950140afa14d4e6ba645070c37
>>>>>>> 6a91b5d423c756b82df34fa1d19ee44af9e1ac77
for k in range(start_size, start_size + validation_size):
    print("k =", k)
    # x_tel = cp.array(x_true) - cp.array(x_k_update_data)
    x_input_data = x_input_data_all[k]
    x_input_data = torch.tensor(cp.hstack(x_input_data), dtype=torch.float32).unsqueeze(0).unsqueeze(0).to(device)
    x_input_tensor = x_input_data.clone().detach().to(device)

    # 使用模型進行推斷
    with torch.no_grad():  # 禁用梯度計算以提高推斷效率
        x_lstm_output = x_lstm_model_loaded(x_input_tensor)  # 獲取模型的輸出
    x_lstm_output_data.append(x_lstm_output.detach().cpu().numpy().flatten())
    print("x LSTM Output:", x_lstm_output[:, :3])  # 輸出結果
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 6a91b5d423c756b82df34fa1d19ee44af9e1ac77
print('-----------------')
print("x =",cp.reshape(cp.array(x_lstm_output_data)[-1, :3], (3, 1)))

# --------P_model loading --------#
# P_lstm_output_data = []
# for k in range(start_size, start_size + validation_size):
#     P_input_data = torch.tensor(cp.hstack(P_input_data_all[k]), dtype=torch.float32).unsqueeze(0).unsqueeze(0).to(device)
#     P_input_tensor = P_input_data.clone().detach().to(device)

#     # 使用模型進行推斷
#     with torch.no_grad():  # 禁用梯度計算以提高推斷效率
#         P_lstm_output = P_lstm_model_loaded(P_input_tensor)  # 獲取模型的輸出
#     P_lstm_output_data.append(P_lstm_output.detach().cpu().numpy().flatten())
# print("P =",cp.reshape(cp.array(P_lstm_output_data)[-1, :9], (3, 3)))
<<<<<<< HEAD
=======
=======

# 解歸一化
# x_lstm_output_data_pd = pd.DataFrame(x_lstm_output_data)
# scaler = MinMaxScaler(feature_range=(0, 1))
# scaler.fit(x_lstm_output_data)
# x_lstm_output_data_denormalized = pd.DataFrame(scaler.inverse_transform(x_lstm_output_data), columns=x_lstm_output_data_pd.columns)
# print("x =",cp.reshape(x_lstm_output_data_denormalized.iloc[-1, :2].to_numpy(), (2, 1)))
print("x =",cp.reshape(cp.array(x_lstm_output_data)[-1, :3], (3, 1)))

# --------P_model loading --------#
# 設置模型參數
input_size = 18  # 根據需要的特徵數
output_size = 9   # 假設輸出有兩個維度

# 加載模型
P_lstm_model_loaded = LSTM.LSTM_KF(input_size, hidden_size, output_size)  # 創建模型實例
P_lstm_model_loaded.load_state_dict(torch.load('motor/motor_model/P_lstm_kf_model.pth', weights_only=True))  # 加載權重
P_lstm_model_loaded.eval()  # 將模型設置為評估模式
P_lstm_model_loaded = P_lstm_model_loaded.to(device)

P_lstm_output_data = []

for k in range(start_size, start_size + validation_size):
    P_input_data = torch.tensor(cp.hstack(P_input_data_all[k]), dtype=torch.float32).unsqueeze(0).unsqueeze(0).to(device)
    P_input_tensor = P_input_data.clone().detach().to(device)

    # 使用模型進行推斷
    with torch.no_grad():  # 禁用梯度計算以提高推斷效率
        P_lstm_output = P_lstm_model_loaded(P_input_tensor)  # 獲取模型的輸出
    P_lstm_output_data.append(P_lstm_output.detach().cpu().numpy().flatten())

# 將數據解歸一化
# P_lstm_output_data_pd = pd.DataFrame(P_lstm_output_data)
# scaler.fit(P_lstm_output_data)
# P_lstm_output_data_denormalized = pd.DataFrame(scaler.inverse_transform(P_lstm_output_data), columns=P_lstm_output_data_pd.columns)
# print("P =",cp.reshape(P_lstm_output_data_denormalized.iloc[-1, :4].to_numpy(), (2, 2)))
print("P =",cp.reshape(cp.array(P_lstm_output_data)[-1, :9], (3, 3)))
>>>>>>> 306d347394907d950140afa14d4e6ba645070c37
>>>>>>> 6a91b5d423c756b82df34fa1d19ee44af9e1ac77

# 先将 cupy 数组转换为 numpy 数组
# x_lstm_output_data_np = x_lstm_output_data.get()
# P_lstm_output_data_np = P_lstm_output_data.get()
x_lstm_output_data_np = x_lstm_output_data
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 6a91b5d423c756b82df34fa1d19ee44af9e1ac77
# P_lstm_output_data_np = P_lstm_output_data
# 使用 numpy.savetxt 将其保存到 txt 文件中
np.savetxt('./result/x_lstm_output_data_motor.txt', x_lstm_output_data_np, delimiter=' ')
# np.savetxt('./result/P_lstm_output_data_motor.txt', P_lstm_output_data_np, delimiter=' ')

# print("Plotting ...")
# 估測狀態匯出
plt.figure()
x_true_noise = x_true
# plt.plot(x_true_noise[start_size:start_size + validation_size], label='True_x1_add_noise', color='black', linewidth=3)
<<<<<<< HEAD
=======
=======
P_lstm_output_data_np = P_lstm_output_data
# 使用 numpy.savetxt 将其保存到 txt 文件中
np.savetxt('./result/x_lstm_output_data_motor.txt', x_lstm_output_data_np, delimiter=' ')
np.savetxt('./result/P_lstm_output_data_motor.txt', P_lstm_output_data_np, delimiter=' ')

# 估測狀態匯出
plt.figure()
x_true_noise = x_true
plt.plot(x_true_noise[start_size:start_size + validation_size], label='True_x1_add_noise', color='black', linewidth=3)
>>>>>>> 306d347394907d950140afa14d4e6ba645070c37
>>>>>>> 6a91b5d423c756b82df34fa1d19ee44af9e1ac77
plt.plot(cp.array(x_k_update_data)[start_size:start_size + validation_size, 0].get(), label='LKF_x1', color='orange', linewidth=2)
plt.plot(cp.array(x_lstm_output_data)[:, 0].get(), label='DKF_x1', color='purple', linewidth=1)
plt.xlabel('data')
plt.ylabel('value')
plt.legend()
plt.title('Pos of estimate vs true')

plt.figure()
x_true_noise = x_true
plt.plot(cp.array(x_k_update_data)[start_size:start_size + validation_size, 1].get(), label='LKF_x2', color='cyan', linewidth=2)
plt.plot(cp.array(x_lstm_output_data)[:, 1].get(), label='DKF_x2', color='red', linewidth=1)
plt.xlabel('data')
plt.ylabel('value')
plt.legend()
plt.title('Vel of estimate vs true')

plt.figure()
x_true_noise = x_true
plt.plot(cp.array(x_k_update_data)[start_size:start_size + validation_size, 2].get(), label='LKF_x3', color='pink', linewidth=2)
plt.plot(cp.array(x_lstm_output_data)[:, 2].get(), label='DKF_x3', color='green', linewidth=1)
plt.xlabel('data')
plt.ylabel('value')
plt.legend()
plt.title('Acc of estimate vs true')

# 估測狀態誤差匯出
x_k_update_data = cp.array(x_k_update_data).reshape(-1, 1)  # reshape to 2D
x_true = cp.array(x_true).reshape(-1, 1)  # reshape to 2D
plt.figure()
a = cp.abs(cp.array(x_k_update_data)[start_size:start_size + validation_size, 0] - cp.array(x_true)[start_size:start_size + validation_size, 0])
<<<<<<< HEAD
plt.plot(a.get(), label='LKF_x1_err', color='black', linewidth=2)
=======
<<<<<<< HEAD
plt.plot(a.get(), label='LKF_x1_err', color='black', linewidth=2)
=======
plt.plot(a.get(), label='LKF_x1', color='black', linewidth=2)
>>>>>>> 306d347394907d950140afa14d4e6ba645070c37
>>>>>>> 6a91b5d423c756b82df34fa1d19ee44af9e1ac77
# b = cp.abs(cp.array(x_k_update_data)[start_size:start_size + validation_size, 1] - cp.array(x_true)[start_size:start_size + validation_size, 1])
# plt.plot(b.get(), label='LKF_x2', color='green', linewidth=2)
# e = cp.abs(cp.array(x_k_update_data)[start_size:start_size + validation_size, 2] - cp.array(x_true)[start_size:start_size + validation_size, 2])
# plt.plot(e.get(), label='LKF_x3', color='purple', linewidth=2)
c = cp.abs(cp.array(x_lstm_output_data)[:, 0] - cp.array(x_true)[start_size:start_size + validation_size, 0])
<<<<<<< HEAD
plt.plot(c.get(), label='DKF_x1_err', color='blue', linewidth=1)
=======
<<<<<<< HEAD
plt.plot(c.get(), label='DKF_x1_err', color='blue', linewidth=1)
=======
plt.plot(c.get(), label='DKF_x1', color='blue', linewidth=1)
>>>>>>> 306d347394907d950140afa14d4e6ba645070c37
>>>>>>> 6a91b5d423c756b82df34fa1d19ee44af9e1ac77
# d = cp.abs(cp.array(x_lstm_output_data)[:, 1] - cp.array(x_true)[start_size:start_size + validation_size, 1])
# plt.plot(d.get(), label='DKF_x2', color='red', linewidth=1)
# f = cp.abs(cp.array(x_lstm_output_data)[:, 2] - cp.array(x_true)[start_size:start_size + validation_size, 2])
# plt.plot(f.get(), label='DKF_x3', color='red', linewidth=1)
plt.xlabel('data')
plt.ylabel('estimate value')
plt.legend()
<<<<<<< HEAD
plt.title('pos error between true_pos')
# print("Finish Plotting ...")
=======
<<<<<<< HEAD
plt.title('pos error between true_pos')
# print("Finish Plotting ...")
=======
plt.title('estimate pos vel acc')
>>>>>>> 306d347394907d950140afa14d4e6ba645070c37
>>>>>>> 6a91b5d423c756b82df34fa1d19ee44af9e1ac77

plt.show()