# Script to convert Excel files to CSV format
library(readxl)
library(writexl)

# Function to convert Excel to CSV
convert_excel_to_csv <- function(input_file, output_file) {
  # Create output directory
  dir.create(dirname(output_file), recursive = TRUE, showWarnings = FALSE)
  
  # Read Excel file and save as CSV
  data <- read_excel(input_file)
  write.csv(data, output_file, row.names = FALSE)
}

# Convert income data
years <- c(2018, 2023)
for (year in years) {
  input_file <- file.path("..", "Data", "raw", "raw_income", 
                         paste0("income", year, "_raw.xlsx"))
  output_file <- file.path("..", "Data", "manual_cleaned", "manual_income", 
                          paste0("income", year, "_manual_cleaned.csv"))
  convert_excel_to_csv(input_file, output_file)
}

# Convert ethnicity data
years <- c(2013, 2018, 2023)
for (year in years) {
  input_file <- file.path("..", "Data", "raw", "raw_ethnicity", 
                         paste0("ethnicity", year, "_raw.xlsx"))
  output_file <- file.path("..", "Data", "manual_cleaned", "manual_ethnicity", 
                          paste0("ethnicity", year, "_manual_cleaned.csv"))
  convert_excel_to_csv(input_file, output_file)
}

# Convert land type data
input_file <- file.path("..", "Data", "raw", "raw_land_type", "land_type_raw.xlsx")
output_file <- file.path("..", "Data", "manual_cleaned", "manual_land_type", 
                        "land_type_manual_cleaned.csv")
convert_excel_to_csv(input_file, output_file) 