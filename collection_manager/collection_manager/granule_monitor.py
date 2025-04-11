import argparse
from collection_manager.services.CollectionWatcher import granule_events

def display_granule_events():
    print("\n=== Granule Events ===")
    for dataset_id, events in granule_events.items():
        print(f"\nDataset ID: {dataset_id}")
        for event in events:
            print(f"  - Path: {event['path']}, Modified Time: {event['modified_time']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monitor granule events in real-time.")
    parser.add_argument("--show", action="store_true", help="Display the current granule events.")
    args = parser.parse_args()

    if args.show:
        display_granule_events()