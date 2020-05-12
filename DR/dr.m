function []=dr()

% This function aims to show your manifold learning method on synthetic
% manifolds, the datsets contain in the software is as follows:
%1.  'Two Swisses'
%2.  'Two Surfaces',1e-4
%3.  'Multi-Surfaces'
%4.  'trefoil'1e-3 %d2=1(d1=0.5 ,532���㣬d1=0.4,665),d2=3(d1=0.1,1131���㣻d1=0.2 ,567���㣻d1=0.3,378����,d1=0.8,144����)(������������ɵ�)
%5.  'S-curve',1e-4;
%6.  'S-curve Noise'noise,1e-2
%7.  'Swiss',1e-6
%8.  'Swiss Hole',1e-4
%9.  'Changing-Swiss',1e-4
%10. 'Sphere',1e-2
%11. 'Helix',1e-3
%12. 'Swiss Connect'
%13. 'S-curve Hole'  % numpoints�ܱ�8������1e-3
%15. '3d-Clusters'
%16. 'Intersect'
%17. 'Tire'1e-4

dataset = {'Two Swisses','Two Surfaces','Multi-Surfaces','trefoil','S-curve','S-curve Noise','Swiss','Swiss Hole','Changing-Swiss','Sphere','Helix','Swiss Connect','S-curve Hole','TwinPeaks','3d-Clusters','Intersect','Tire'};
tol = [1e-3,1e-4,1e-4,1e-3,1e-3,1e-4,1e-4,1e-4,1e-4,1e-2,1e-2,1e-4,1e-3,1e-4,1e-3];

numpoints = 300;            % �������ݵ�ĸ���

% ѡ����Ҫ�Աȵķ���
alg = {'LLE', 'HLLE', 'LLC', 'LTSA', 'MLLE', 'IHNE', 'RHNE', 'BHNE'};       %  , 'CorrLLEO',
col = length(alg);
row = 8;                    % ��ͼ������
no_dims =2;                 % ��άά��

for p = 2                   % ѡ�����ݼ�
    dataname=dataset{p};
    if strcmp(dataname,'trefoil')
        [X, labels] = generate_data(dataname,numpoints,0.8,3);
    else
        [X, labels] = generate_data(dataname,numpoints);
    end 
    
    % �����ά������label
    save(['./data/X_p=', num2str(p), '.mat'], 'X');
    save(['./data/labels_p=', num2str(p), '.mat'], 'labels');

    scatter3(X(:,1), X(:,2), X(:,3), 23, labels,'.');
    axis tight;
    set(gca,'xtick',[],'ytick',[],'ztick',[]);
    grid off;
    box on;
    zlabel(dataname,'FontSize',15);

    figure
    for i=1:row
        k=3+i;              % ����k����ʼ��С
        for j=1:col
            subplot(row,col,(i-1)*col+j)
            [mappedX]= compute_mapping(X, alg{j}, no_dims, k,tol(p));
            save(['./data/Y_p=', num2str(p), '_', alg{j}, '_k=', num2str(k), '.mat'], 'mappedX');
            scatter(mappedX(:,1), mappedX(:,2), 23, labels,'.');
            axis tight;
            set(gca,'xtick',[],'ytick',[]);
            box on;
            if j==1
                ylabel(strcat('k=',num2str(k)),'FontSize',15);
            end
            if i==row
                xlabel(alg{j},'FontSize',15);
            end
        end
    end
end