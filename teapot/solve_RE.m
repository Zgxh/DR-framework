function []=solve_RE()

% load data
load teapot.mat
dataname='teapot';
teapots=X;
m=400; % 400��ͼ��
indx=1:400;
data=teapots(:,indx(1:2:m)); % ȡ200��������ÿ����������ȡһ��

row=1;
err = zeros(5,row); % ͳ��5�ַ������ؽ����

%%%%%%%%%%%%%%%% ���ع���� n=200        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%% ��״ͼ���ӻ���ʵ�� k=4      %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%% �ؽ���� Table k=4~8      %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%% �ؽ��������ͼ k=2~20    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
for i=1:row

      K=4;

     % �������� LLE
     [poses] = Rec_LLE(data,K);
     tempErr = sqrt(sum((poses-data).^2,1));
     err(1,i) = mean(tempErr);

     % ����3�� MLLE
     [poses] = Rec_MLLE(data,K);
     tempErr = sqrt(sum((poses-data).^2,1));
     err(2,i)=mean(tempErr);

     % ����4�� INV_HNE
     [poses]=Rec_IHNE(data,K);
     tempErr = sqrt(sum((poses-data).^2,1));
     err(3,i)=mean(tempErr);

     % ����5�� REC_HNE
     [poses]=Rec_RHNE(data,K);
     tempErr = sqrt(sum((poses-data).^2,1));
     err(4,i)=mean(tempErr);

     % ����6�� BAL_HNE
     [poses]=Rec_BHNE(data,K);
     tempErr = sqrt(sum((poses-data).^2,1));
     err(5,i)=mean(tempErr);

     % ��ӡRE
     err

end