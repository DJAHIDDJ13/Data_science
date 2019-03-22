% TP2
%% Exercice1
x = [1, 2];
h = [1, 0, 0, 1];


F = [x,zeros(1,length(x))];
G = [h,zeros(1,length(h))];

y = zeros(1, length(x) + length(h) - 1);
for i=1:length(h)+length(x)-1
    for j=1:length(x)
        if(i-j+1>0)
            y(i) = y(i) + F(j) * G(i-j+1);
        end
    end
end

X=0:length(x)+length(h)-2; % i = 0; j = len(f) + len(g)

subplot(1,2,1);
stem(X, y);

subplot(1,2,2);
conv_res = conv(x, h); % convolution matlab
stem(X, conv_res);

% pas de difference entre les deux

%% Question4
 
[orig_audio, orig_fs] = audioread('./TP2wav/Original.wav');

sound(orig_audio, orig_fs);


%% Question5
[ambp_audio, ambp_fs] = audioread('./TP2wav/AmbiancePiece.wav');
h = [ 1, 0, 0, 0, 1];
ambp_audio = ambp_audio(:,1);

ambp_out = conv(ambp_audio, h);
% Question6
audiowrite('TP2wav/Output.wav', ambp_out, ambp_fs);

%% Question7
[ambp_audio, ambp_fs] = audioread('./TP2wav/AmbiancePiece.wav');
h = [ 1, 0, 0, 0, 1];
ambp_audio = ambp_audio(:,1);

ambp_out = conv(ambp_audio, h);

