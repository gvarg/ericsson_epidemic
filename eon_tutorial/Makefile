DOCKER_IMAGE = python3-eon
DOCKER_CONTAINER = eon_env

.PHONY: image
image:
	docker build \
	-f Dockerfile \
	--tag $(DOCKER_IMAGE) \
	.

.PHONY: container
container:
	docker run -it --rm -d \
	--name $(DOCKER_CONTAINER) \
	--memory 5G \
	-v $(CURDIR):/project \
	$(DOCKER_IMAGE)

.PHONY: bash
bash:
	docker exec -it $(DOCKER_CONTAINER) bash

.PHONY: simulation
simulation:
	docker exec -it $(DOCKER_CONTAINER) python3 /project/SIR_simulation.py