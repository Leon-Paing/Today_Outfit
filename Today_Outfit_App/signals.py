import csv
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import FashionItem

@receiver(post_save, sender=FashionItem)
def update_csv_on_save(sender, instance, **kwargs):
    # Define the path to your CSV file
    csv_file_path = 'Today_Outfit/Today_Outfit_App/OutfitDataset.csv'
    
    # Open the CSV file in append mode
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write the new item to the CSV file
        writer.writerow([
            instance.gender,
            instance.category,
            instance.item_type,
            instance.description
        ])
