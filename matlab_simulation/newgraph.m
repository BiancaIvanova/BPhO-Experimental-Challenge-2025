g = 9.81;
dt = 0.0005;
c1 = 0.8; % Coefficient of Restitution for football
c2 = 0.8; % Coefficient of Restitution for tennis ball
m1 = 432.83; % Mass of football in g
m2 = 58.94;  % Mass of tennis ball in g 

h1_values = [];
h2_values = [];
v1_values = [];
v2_values = [];

for h1 = 0.5:0.1:1.4
    h2 = h1 + 0.1;
    v1 = 0;
    v2 = 0;
    time = 0;
    h1_max = h1;
    h2_max = h2;
    v1_max = v1;
    v2_max = v2;
    
    while time < 10
        h1 = h1 - (v1 * dt) + (0.5 * g * dt^2);
        v1 = v1 + g * dt;
        h2 = h2 - (v2 * dt) + (0.5 * g * dt^2);
        v2 = v2 + g * dt;
        
        if h1 < 0
            h1 = 0;
            v1 = -v1 * c1;
        end
        
        if h2 < h1 + 0.09
            h2 = h1 + 0.1;
            v2Final = ((m2 - m1) / (m1 + m2)) * v2 + ((2 * m1) / (m1 + m2)) * v1;
            v2 = v2Final * c2;
        end
        
        h1_max = max(h1_max, h1);
        h2_max = max(h2_max, h2);
        v1_max = max(v1_max, v1);
        v2_max = max(v2_max, v2);
        
        time = time + dt;
    end
    
    h1_values = [h1_values, h1_max];
    h2_values = [h2_values, h2_max];
    v1_values = [v1_values, v1_max];
    v2_values = [v2_values, v2_max];
end

figure(1);
hold on;
title("Max Height of Football against Max Height of Tennis Ball");
xlabel("Max Height of Football (m)");
ylabel("Max Height of Tennis Ball (m)");
plot(h1_values, h2_values, 'k-o', MarkerSize = 5, MarkerFaceColor = 'blue');
grid on;
hold off;

figure(2);
hold on;
title("Max Velocity of Football against Max Velocity of Tennis Ball");
xlabel("Max Velocity of Football / ms^-1");
ylabel("Max Velocity of Tennis Ball / ms^-1");
plot(v1_values, v2_values, 'k-o', MarkerSize = 5, MarkerFaceColor = 'red');
grid on;
hold off;