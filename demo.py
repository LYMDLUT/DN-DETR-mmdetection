from mmdet.apis import init_detector, inference_detector

config_file = 'configs/detr/detr_r50_8x2_150e_coco_focal.py'
checkpoint_file = 'detr_r50_8x2_150e_coco.pth'
model = init_detector(config_file, checkpoint_file, device='cuda:0')  # or device='cuda:0'
inference_detector(model, 'demo/demo.jpg')