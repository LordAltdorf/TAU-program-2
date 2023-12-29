#Ссылка на документацию https://docs.google.com/document/d/1Z5xmv1l57BpwuL4hIF0nAWLaipCuIau5JSWB4Qfo7sA/edit?usp=sharing

import control
import matplotlib.pyplot as plt
import numpy as np

# Передаточные функции
# Апериодическое звено, коэффициент усиления К = 2, постоянная времени Т = 1
K = 2
T = 1
tf1 = control.TransferFunction([K], [T, 1])  # W(s) = 2/(s + 1)
tf2 = control.TransferFunction([3], [1, 2, 1])  # W(s) = 3/(s^2 + 2s + 1)
tf3 = control.TransferFunction([1], [1, 0])  # W(s) = 1/s
tf4 = control.TransferFunction([1, 0], [1, 0, 0])  # W(s) = s

# Пример использования передаточной функции
# Построение графика ЛАХ для tf1
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

# построение асимптот для ЛАХ
fig = plt.figure()
mag, phase, omega = control.bode_plot(tf1, dB = True, Hz = False)

wL0 = np.interp(1, np.flipud(mag), np.flipud(omega))

ax1,ax2 = plt.gcf().axes     # get subplot axes

plt.sca(ax1)                 # построение асимптот амплитуды
plt.plot([1/T, 1/T], plt.ylim(),'r--')
plt.plot(plt.xlim(),[20*np.log10(2), 20*np.log10(2)],'--', color = 'orange')
plt.plot((omega), +20*np.log10(K) - 20*np.log10(T) - 20*np.log10(omega), '--', color = 'orange')

plt.sca(ax2)                 # построение асимптоты фазы
plt.plot(plt.xlim(),[-90,-90],'r--')
plt.plot([1/T, 1/T], plt.ylim(),'r--')
