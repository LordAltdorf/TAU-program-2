#Ссылка на документацию https://docs.google.com/document/d/1Z5xmv1l57BpwuL4hIF0nAWLaipCuIau5JSWB4Qfo7sA/edit?usp=sharing

import control
import matplotlib.pyplot as plt

# Передаточные функции
tf1 = control.TransferFunction([2], [1, 1])  # W(s) = 2/(s + 1)
tf2 = control.TransferFunction([3], [1, 2, 1])  # W(s) = 3/(s^2 + 2s + 1)
tf3 = control.TransferFunction([1], [1, 0])  # W(s) = 1/s
tf4 = control.TransferFunction([1, 0], [1, 0, 0])  # W(s) = s

# Пример использования передаточной функции
# Построение графика Лапласа для tf1
plt.figure()
control.bode_plot(tf1)

# Построение графика Лапласа для tf2
plt.figure()
control.bode_plot(tf2)

# Построение графика Лапласа для tf3
plt.figure()
control.bode_plot(tf3)

# Построение графика Лапласа для tf4
plt.figure()
control.bode_plot(tf4)

plt.show()