shear_image, rotated_image, scaled_image, original_image = image_translation(0.3, 45, [1.2, 1.2])

if shear_image is not None and rotated_image is not None and scaled_image is not None:
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))

    axs[0, 0].imshow(shear_image)
    axs[0, 0].set_title('Shear')
    axs[0, 0].axis('off')

    axs[0, 1].imshow(rotated_image)
    axs[0, 1].set_title('Rotation')
    axs[0, 1].axis('off')

    axs[1, 0].imshow(scaled_image)
    axs[1, 0].set_title('Scaled')
    axs[1, 0].axis('off')
    
    original_image_rgb = cv.cvtColor(original_image, cv.COLOR_BGR2RGB)
    axs[1, 1].imshow(original_image_rgb)
    axs[1, 1].set_title('Original')
    axs[1, 1].axis('off')

    plt.show()