function []=Epoch_BHNE()

% load data
load teapot.mat
dataname='teapot';
teapots=X;
m=400; % 400张图像
indx=1:400;
data=teapots(:,indx(1:2:m)); % 取200个样本，每两个样本中取一个

%%%%%%%%%%  求重构的平均误差  %%%%%%%%%%%%%%%%
row=8;
EPOCH = 20;
err = zeros(row, EPOCH/2);
for i=1:row

     K = 1 + i;
     disp(['k=',num2str(K)]);
  
     for epoch=2:2:EPOCH
        [poses]=BHNE_epoch_var(data,K,epoch);
        tempErr = sqrt(sum((poses-data).^2,1));
        err(i,epoch/2)=mean(tempErr);
        err
     end
end
