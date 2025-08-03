# Script to process ethnicity data for all years
library(dplyr)

# Function to process data for a specific year
process_ethnicity_data <- function(year) {
  # Set file paths
  input_file <- file.path("..", "Data", "manual_cleaned", "manual_ethnicity", 
                         paste0("ethnicity", year, "_manual_cleaned.csv"))
  output_file <- file.path("..", "Data", "cleaned", "final_ethnicity", 
                          paste0("ethnicity_", year, ".csv"))
  
  # Create output directory
  dir.create(dirname(output_file), recursive = TRUE, showWarnings = FALSE)
  
  # Read and process data
  data <- read.csv(input_file) %>%
    mutate(
      suburb = trimws(suburb),
      suburb = gsub(" \\(Christchurch City\\)", "", suburb),
      suburb = trimws(suburb)
    ) %>%
    mutate(across(c(european, maori, pacific_peoples, asian, 
                   middle_eastern_latin_american_african, other_ethnicity_nec, 
                   new_zealander, total_ethnicity),
                 ~ifelse(is.na(.) | . == "", NA_real_, 
                        as.numeric(gsub("[^0-9.]", "", .))))) %>%
    mutate(
      suburb = case_when(
        suburb == "Burnside" ~ "Burnside One",
        suburb == "Christchurch Central" ~ "Christchurch Central One",
        suburb == "Islington" ~ "Islington One",
        TRUE ~ suburb
      )
    )
  
  # Define suburbs for processing
  suburbs <- c("Addington", "Avonhead", "Awatea", "Belfast", "Bishopdale", "Banks Peninsula",
               "Bromley", "Bryndwr", "Burnside", "Burwood", "Cashmere", "Christchurch Central",
               "Edgeware", "Halswell", "Hoon Hay", "Hornby", "Ilam", "Islington", "Linwood",
               "Mairehau", "Oaklands", "Papanui", "Prestons", "Redwood", "Riccarton",
               "Richmond", "Shirley", "Sockburn", "Somerfield", "Spreydon", "Saint Albans",
               "Sydenham", "Wigram", "Woolston")
  
  # Process suburbs and calculate statistics
  final_data <- data
  for (suburb_name in suburbs) {
    # Match using base name without "One"
    base_name <- gsub(" One$", "", suburb_name)
    matching_rows <- data %>% filter(grepl(base_name, .data$suburb))
    if(nrow(matching_rows) == 0) next
    
    # Calculate summary data
    totals <- matching_rows %>%
      summarise(
        european = sum(european, na.rm = TRUE),
        maori = sum(maori, na.rm = TRUE),
        pacific_peoples = sum(pacific_peoples, na.rm = TRUE),
        asian = sum(asian, na.rm = TRUE),
        middle_eastern_latin_american_african = sum(middle_eastern_latin_american_african, na.rm = TRUE),
        other_ethnicity_nec = sum(other_ethnicity_nec, na.rm = TRUE),
        new_zealander = sum(new_zealander, na.rm = TRUE),
        total_ethnicity = sum(total_ethnicity, na.rm = TRUE),
        suburb = suburb_name
      )
    
    # Insert summary data
    last_index <- max(which(grepl(base_name, data$suburb)))
    final_data <- bind_rows(
      final_data[1:last_index, ],
      totals,
      final_data[(last_index + 1):nrow(final_data), ]
    )
  }
  
  # Calculate final statistics and save
  final_data %>%
    mutate(
      year = year,
      # Calculate percentages
      european_pct = european / total_ethnicity,
      maori_pct = maori / total_ethnicity,
      pacific_peoples_pct = pacific_peoples / total_ethnicity,
      asian_pct = asian / total_ethnicity,
      middle_eastern_latin_american_african_pct = middle_eastern_latin_american_african / total_ethnicity,
      other_ethnicity_nec_pct = other_ethnicity_nec / total_ethnicity,
      new_zealander_pct = new_zealander / total_ethnicity
    ) %>%
    write.csv(output_file, row.names = FALSE)
  
  return(final_data)
}

# Process data for all years
years <- c(2013, 2018, 2023)
for (year in years) {
  process_ethnicity_data(year)
} 