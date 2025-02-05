    g = 9.81;
    dt = 0.0005;
    v1 = 0;
    %h1 = input("What height would you like the football to drop from?     ");
    h1 = 1.5; % Drop Height
    v2 = 0;
    h2 = h1+0.1;
    %c1 = input("What would you like the coefficient of restitution to be for the football?   ");
    %c2 = input("What would you like the coefficient of restitution to be for the tennis ball?    ");
    c1 = 0.8; % Coefficient of Restitution
    c2 = 0.8;
    m1 = 432.83; % Mass of football in g
    m2 = 58.94; % Mass of tennis ball in g
    time = 0;
    % Plotting the simulation
   
    hold on;    

    axis([0 1 0 h2+8]);
    
    title("Gravitational Slingshot");
    ylabel("Height / m");
    
    % Actual dropping phyiscs
    
    h1 = h1 - (v1*dt) + (0.5*g*dt^2);
    h2 = h2 - (v2*dt) + (0.5*g*dt^2);
    v1 = v1 + g*dt;
    v2 = v2 + g*dt;
    ball2 = plot([0.5], h2, 'bo', markerFaceColor='b');
    ball1 = plot([0.5], h1, 'ro', markerFaceColor='r', markerSize = 15);

    while time<10

        hold on;
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

        set(ball1, 'YData', h1);
        set(ball2, 'YData', h2);

        time = time+dt;

        pause(dt);

    end
    