    g = 9.81;
    dt = 0.0005;
    v1 = 0;
    %h1 = input("What height would you like the football to drop from?  ");
    h1 = 1; % Drop Height
    v2 = 0;
    h2 = h1+0.1;
    c1 = 0.8; %Coefficient of Restitution
    c2 = 0.8;
    %c1 = input("What would you like the coefficient of restitution to be for the football?   ");
    %c2 = input("What would you like the coefficient of restitution to be for the tennis ball?    ");
    m1 = 432.83; % Mass of football in g
    m2 = 58.94; % Mass of tennis ball in g 
    time_values = [];
    v1_values = [];
    v2_values = [];
    h1_values = [];
    h2_values = [];
    
    time = 0;
    % Actual dropping phyiscs
    
    h1 = h1 - (v1*dt) + (0.5*g*dt^2);
    h2 = h2 - (v2*dt) + (0.5*g*dt^2);
    
    v1 = v1 + g*dt;
    v2 = v2 + g*dt;
    
    
    while time<10
        
        
        h1 = h1 - (v1*dt) + (0.5*g*dt^2);
        v1 = v1 + g*dt;
        h2 = h2 - (v2*dt) + (0.5*g*dt^2);
        v2 = v2 + g*dt;
        
        if(h1<0)
            h1 = 0;
           
            v1 = -v1*c1;
            
        end
        
        if (h2<h1+0.09)
            h2 = h1+0.1;
            v2Final = ((m2 - m1) / (m1 + m2)) * v2 + ((2 * m1) / (m1 + m2)) * v1;
            v2 = v2Final * c2;
        end

        time_values = [time_values, time];
        v1_values = [v1_values, v1];
        v2_values = [v2_values, v2];
        h1_values = [h1_values, h1];
        h2_values = [h2_values, h2];
        time = time+dt;

    end

    figure(1);
    hold on;
    title("Velocity Graph of Gravitational Slingshot");
    xlabel("Time Taken / s");
    ylabel("Velocity / ms^-1");
    plot(time_values, v1_values, 'b-', LineWidth = 2.5);
    plot(time_values, v2_values, 'r-', LineWidth = 1.5);
    legend("Football", "Tennis Ball");
    grid();
    hold off;
   
    figure(2);
    hold on;
    title("Velocity of Football against Velocity of Tennis Ball");
    xlabel("Velocity of Football");
    ylabel("Velocity of Tennis Ball");
    plot(v1_values, v2_values, 'ko', MarkerSize = 1);
    grid();
    hold off;

    figure(3);
    hold on;
    title("Height Graph of Gravitational Slingshot");
    xlabel("Time Taken / s");
    ylabel("Height / m");
    plot(time_values,h1_values,'b-',LineWidth = 2.5);
    plot(time_values, h2_values,'r-', LineWidth = 1.5);
    legend("Football","Tennis Ball");
    grid();
    hold off;

    figure(4);
    hold on;
    title("Height of Football against Height of Tennis Ball");
    xlabel("Height of Football / m");
    ylabel("Height of Tennis Ball / m");
    plot(h1_values, h2_values, 'ko', MarkerSize = 1);
    grid();
    hold off;
