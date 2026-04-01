variable "render_api_key" {
  description = "Render API Key"
  type        = string
  sensitive   = true
}

variable "render_owner_id" {
  description = "Render Owner ID"
  type        = string
}

variable "github_actor" {
  description = "GitHub username"
  type        = string
}

variable "image_url" {
  description = "Docker image URL"
  type        = string
}

variable "image_tag" {
  description = "Docker image tag"
  type        = string
}

variable "database_url" {
  description = "PostgreSQL connection URL"
  type        = string
  sensitive   = true
}
