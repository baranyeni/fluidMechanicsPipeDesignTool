#!/usr/bin/env python

import math
import matplotlib.pyplot as plot

class Calculate():
    def main(self, gNumber = 8):
        firstDim = float(input('Dim range first : '))
        lastDim = float(input('Dim range last  : '))

        L = 1000 + (gNumber * 50)                  # Length of the piping system
        T = 5 + (gNumber * 0.25)                   # Height of discharge P_kWint from the lake and tank in distribution center
        fLoss = 0.0003 * (gNumber + 50)            # Roughness of the pipe
        p  = 997                                   # Density of the fluid
        g  = 9.81                                  # Gravity
        k  = 10.6 #5                               # Friction factor of piping system element
        g  = 9.81                                  # Gravity
        lt = 0.01 * L                              # Length of the tank
        ht = 0.20 * T                              # Height of tank from baseline to the top of double bottom
        bt = 0.50 * lt                             # Beam of the tank
        t  = 10000/((g/ht)**.5)                    # Time
        Q  = (lt * ht * bt) / t                    # Flow rate
        Viscosity = 0.001308                       # Dynamic viscosity
        Power, Cost, H_Loss, Dim = [], [], [], []  # Tuples to collect whole graph data

        print("L =", L)
        print("T =", T)
        print("ht =", ht)
        print("lt =", lt)
        print("bt =", bt)
        print("t =", t)
        print("Q =", Q)

        if lastDim < firstDim:
            tempVariable = lastDim
            lastDim = firstDim
            firstDim = tempVariable

        while firstDim <= lastDim:
            D = firstDim
            A = math.pi*((D/2)**2)                 # Area of pipe
            V = Q/A                                # Velocity of fluid

            Re = (p*V*D)/Viscosity

            if Re <= 4000:
                f = 64/Re
            else:
                f = (1/(-1.8*(math.log10((((fLoss/D)/3.7)**1.11)+(6.9/Re)))))**2

            H1 = f*(L/D)*((V**2)/(2*g))
            H2 = k*((V**2)/(2*g))     
            Ht = H1+H2+T                           # Total headloss

            P_kW = (p*Q*g*Ht)/1000                 # Power

            Elc   = (t*2*5*365*0.1*P_kW)/3600      # Electricity Cost
            pam   = 3500+(100*Ht)                  # Pump and motor
            val   = 6*(300+(200*D/0.025))          # Valves
            elb   = 4*(50+(50*D/0.025))            # Elbows
            pps   = L*(D/0.025)                    # Pipes
            Total_Cost = Elc+pam+val+elb+pps       # Total Cost

            Power.append(P_kW)
            Cost.append(Total_Cost)
            H_Loss.append(Ht)
            Dim.append(D)

            firstDim = firstDim + 0.01             # Sample frequency
        self.drawGraph(Dim, Power, H_Loss, Cost)

    def drawGraph(self, Dimension, Power, Headloss, Cost):
        print(Dimension, Power, Headloss, Cost)
        plot.figure(num='Furkan Emre Durmus')
        plot.subplots_adjust(wspace=.5, hspace=.75)
        plot.style.use('ggplot')

        plot.subplot(2, 2, 2)
        plot.plot(Dimension, Power)
        plot.xlabel("Dim (m)")
        plot.ylabel("Power (kW)")
        plot.title("Power - Dim", y=1.15)
        plot.grid(linestyle = '--')

        plot.subplot(2, 2, 1)
        plot.plot(Dimension, Cost)
        plot.xlabel("Dim (m)")
        plot.ylabel("Total Cost ($)")
        plot.title("Total cost - Dimension", y=1.15)
        plot.grid(linestyle = '--')

        plot.subplot(2, 2, 3)
        plot.plot(Dimension, Headloss)
        plot.xlabel("Dimension (m)")
        plot.ylabel("Headloss")
        plot.title("Headloss - Dimension", y=1.15)
        plot.grid(linestyle = '--')

        plot.show()

if __name__ == '__main__':
    Calculate().main()

