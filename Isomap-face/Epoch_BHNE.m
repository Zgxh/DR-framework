function []=Epoch_BHNE()

load face_data.mat;
m=698;
data=images(:,1:m);

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
