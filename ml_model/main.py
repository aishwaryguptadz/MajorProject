"""
SyntheticAI – Smart Maritime Route Optimization System
CLI entry point for training models and finding optimal routes.

Usage:
    # Train models
    python main.py train

    # Train models (fast, no GridSearch)
    python main.py train --fast

    # Find best routes
    python main.py route --origin "Jebel Ali" --destination "Guangzhou" --ship_type "Tanker"

    # List available ports
    python main.py ports
"""
import argparse
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))


def cmd_train(args):
    """Train both fuel and ETA models."""
    from train_fuel_model import main as train_fuel
    from train_eta_model import main as train_eta

    print("\n" + "█" * 60)
    print("  SyntheticAI – Training Pipeline")
    print("█" * 60)

    tune = not args.fast
    if args.fast:
        print("\n  ⚡ Fast mode: skipping GridSearchCV\n")

    print("\n─── STEP 1/2: Fuel Prediction Model ───")
    fuel_model, fuel_metrics = train_fuel(tune=tune)

    print("\n─── STEP 2/2: ETA Prediction Model ───")
    eta_model, eta_metrics = train_eta(tune=tune)

    print("\n" + "█" * 60)
    print("  TRAINING COMPLETE")
    print("█" * 60)
    print(f"\n  Fuel Model R²:  {fuel_metrics['r2']:.4f}")
    print(f"  ETA  Model R²:  {eta_metrics['r2']:.4f}")
    print(f"\n  Models saved to: models/")
    print(f"  Evaluation plots saved to: evaluation/")
    print("█" * 60)


def cmd_route(args):
    """Find optimal routes between two ports."""
    from predict import MaritimePredictor

    predictor = MaritimePredictor()
    routes = predictor.recommend_routes(
        origin=args.origin,
        destination=args.destination,
        ship_type=args.ship_type,
        top_k=3,
    )

    if not routes:
        print(f"\n❌ No routes found from {args.origin} to {args.destination}")
        ports = predictor.get_ports()
        print(f"\nAvailable origins: {', '.join(ports['origins'])}")
        print(f"Available destinations: {', '.join(ports['destinations'])}")


def cmd_ports(args):
    """List all available ports."""
    from predict import MaritimePredictor

    predictor = MaritimePredictor()
    ports = predictor.get_ports()

    print("\n" + "=" * 50)
    print("  Available Ports")
    print("=" * 50)
    print(f"\n  Origin Ports ({len(ports['origins'])}):")
    for p in ports['origins']:
        print(f"    • {p}")
    print(f"\n  Destination Ports ({len(ports['destinations'])}):")
    for p in ports['destinations']:
        print(f"    • {p}")
    print("=" * 50)


def main():
    parser = argparse.ArgumentParser(
        description='SyntheticAI – Smart Maritime Route Optimization',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py train                     Train both models
  python main.py train --fast              Train without GridSearch
  python main.py route -o "Jebel Ali" -d "Guangzhou" -s "Tanker"
  python main.py ports                     List available ports
        """
    )
    subparsers = parser.add_subparsers(dest='command', help='Command to run')

    # Train command
    train_parser = subparsers.add_parser('train', help='Train fuel & ETA models')
    train_parser.add_argument('--fast', action='store_true',
                              help='Skip GridSearchCV for quick training')

    # Route command
    route_parser = subparsers.add_parser('route', help='Find best routes')
    route_parser.add_argument('-o', '--origin', required=True, help='Origin port name')
    route_parser.add_argument('-d', '--destination', required=True, help='Destination port name')
    route_parser.add_argument('-s', '--ship_type', default=None, help='Ship type filter')

    # Ports command
    subparsers.add_parser('ports', help='List available ports')

    args = parser.parse_args()

    if args.command == 'train':
        cmd_train(args)
    elif args.command == 'route':
        cmd_route(args)
    elif args.command == 'ports':
        cmd_ports(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
