import csv

def write_to_csv(model_name, regularization, balancer, train_acc, train_loss, valid_acc, valid_loss, test_acc, test_loss, file_name="Model_evaluation.csv"):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Model Name', 'Regularization', 'Balancer', 'Train Accuracy', 'Train Loss', 'Valid Accuracy', 'Valid Loss', 'Test Accuracy', 'Test Loss'])
        writer.writerow([model_name, regularization, balancer, train_acc, train_loss, valid_acc, valid_loss, test_acc, test_loss])
