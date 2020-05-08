function []=compare_I_B()

load face_data.mat;
m=698;
data=images(:,1:m);

%%%%%%%%%%%%%%%%%%  �Ƚ�IHNE��BHNE��ÿ��ͼ����ؽ��ϵ�Ч��  %%%%%%%%%%%%%%%%
row=8;
count = zeros(1, row);
IHNE_error = zeros(row, 698);
BHNE_error = zeros(row, 698);
for i=1:row

     K = i + 1;
     disp(['k=',num2str(K)]);
     
     % IHNE
     [poses]=Rec_IHNE(data,K);
     IHNE_error(i, :) = sqrt(sum((poses-data).^2,1));
     
     %  BHNE
     [poses]=Rec_BHNE(data,K);
     BHNE_error(i, :) = sqrt(sum((poses-data).^2,1));
     
     count(1, i) = sum(BHNE_error(i, :) < IHNE_error(i, :))/698;  % BHNE��IHNE�ؽ����С��ͼ�����
     
     count
     
end

% save IHNE_error;
% save BHNE_error;
% save count;