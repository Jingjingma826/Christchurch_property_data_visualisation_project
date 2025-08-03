# Script to process property data for all years
# Load required libraries
library(dplyr)
library(stringr)

# Function to process data for a specific year
process_property_data <- function(year) {
  # Set file paths
  input_file <- file.path("..", "Data", "manual_cleaned", "manual_property", 
                         "property_selected_years_maunual_cleaned.csv")
  output_file <- file.path("..", "Data", "cleaned", "final_property", 
                          paste0("property_", year, ".csv"))
  
  # Create output directory
  dir.create(dirname(output_file), recursive = TRUE, showWarnings = FALSE)
  
  # Read and process data
  data <- read.csv(input_file) %>%
    # Clean suburb names by removing whitespace
    mutate(suburb = str_trim(suburb)) %>%
    # Process price data
    mutate(
      total_value = case_when(
        is.na(total_value) | total_value == "" ~ NA_real_,
        # Handle scientific notation (e.g., 1M)
        str_detect(total_value, "M") ~ as.numeric(str_replace_all(total_value, "[M\\s]", "")) * 1000000,
        # Handle K notation
        str_detect(total_value, "K") ~ as.numeric(str_replace_all(total_value, "[K\\s]", "")) * 1000,
        # Handle regular numbers
        TRUE ~ as.numeric(str_replace_all(total_value, "[\\s]", ""))
      )
    ) %>%
    filter(sale_year == year) %>%
    # Group by suburb to handle duplicate records
    group_by(suburb) %>%
    reframe(
      year = first(sale_year),
      sales_count = n(),
      # Use non-NA median price
      median_price = if(all(is.na(total_value))) NA_real_ else median(total_value, na.rm = TRUE)
    ) %>%
    # Ensure no duplicate suburb names
    group_by(suburb) %>%
    summarise(
      year = first(year),
      sales_count = sum(sales_count),
      median_price = first(median_price)
    ) %>%
    arrange(suburb)
  
  # Print processing information
  cat(sprintf("\nProcessing data for year %d:\n", year))
  cat(sprintf("Total number of suburbs: %d\n", nrow(data)))
  cat(sprintf("Number of suburbs with missing median prices: %d\n", sum(is.na(data$median_price))))
  if(sum(is.na(data$median_price)) > 0) {
    cat("Suburbs with missing median prices:\n")
    print(data$suburb[is.na(data$median_price)])
  }
  
  # Save results
  write.csv(data, output_file, row.names = FALSE)
  return(data)
}

# Process data for all years
years <- c(2013, 2018, 2023)
for (year in years) {
  process_property_data(year)
}

cat("\nData processing completed for all years!\n") 