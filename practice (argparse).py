import argparse  # Make sure argparse is properly imported

# Create ArgumentParser object
parser = argparse.ArgumentParser(description='A simple CLI example')

# Add the input_file argument (required)
parser.add_argument('input_file', help='The input file to process')

# Add the verbose argument (optional)
parser.add_argument('--verbose', action='store_true', help='Enable verbose output')

# Parse arguments
args = parser.parse_args()

# Print verbose value
print('Verbose:', args.verbose)

